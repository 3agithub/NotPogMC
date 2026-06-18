import datetime
import discord
from discord.ext import commands
import random
from random import randint
from loot_tables import ADVENTURE as LOOT_TABLES

MULTI_DISCOVERY_CHANCE = 0.15

def loot_num(min_val, max_val):
    res = randint(0, 1000)
    final_amt = round(res / 1000 * (max_val - min_val) + min_val)
    return [final_amt, res]

def run_adventure_action(dimension: str, target_biome: str = None) -> dict:
    dim_data = LOOT_TABLES.get(dimension.lower())
    if not dim_data:
        return {"error": "Invalid dimension specified."}

    biomes_pool = list(dim_data["biomes"].keys())
    
    if target_biome and target_biome in biomes_pool:
        selected_biome = target_biome
    else:
        biome_weights = [dim_data["biomes"][b]["weight"] for b in biomes_pool]
        total_biome_weight = sum(biome_weights)
        biome_roll = randint(1, total_biome_weight)
        
        current_biome_sum = 0
        selected_biome = biomes_pool
        for biome, w in zip(biomes_pool, biome_weights):
            current_biome_sum += w
            if biome_roll <= current_biome_sum:
                selected_biome = biome
                break

    allowed_structures = dim_data["biomes"][selected_biome]["allowed_structures"]

    if random.random() < MULTI_DISCOVERY_CHANCE:
        structures_found_count = randint(2, 3)
    else:
        structures_found_count = 1
        
    discovered_structures = []
    struct_weights = [dim_data["structures"][s]["weight"] for s in allowed_structures]
    total_struct_weight = sum(struct_weights)

    for _ in range(structures_found_count):
        roll = randint(1, total_struct_weight)
        current_struct_sum = 0
        for struct, w in zip(allowed_structures, struct_weights):
            current_struct_sum += w
            if roll <= current_struct_sum:
                discovered_structures.append(struct)
                break
    
    discovered_names = [s for s in discovered_structures if s != "none"]
    valid_choices = [s for s in discovered_structures if s != "none"]
    
    if not valid_choices:
        selected_structure = "none"
    else:
        selected_structure = valid_choices[randint(0, len(valid_choices) - 1)]

    if selected_structure == "none":
        return {
            "biome": selected_biome,
            "structure": "none",
            "chests": 0,
            "drops": [],
            "discovered": []
        }

    struct_config = dim_data["structures"][selected_structure]
    aggregated_drops = {}
    
    if struct_config.get("unique_chests", False):
        all_possible_chests = ["map", "supply", "treasure"]
        num_chests = randint(2, 3)
        
        chests_to_raid = random.sample(all_possible_chests, k=num_chests)
        
        for chest_type in chests_to_raid:
            pool_registry_id = f"{selected_structure.replace(' ', '_')}_{chest_type}_pools"
            active_pools = dim_data["loot_pools"][pool_registry_id]
            
            for pool in active_pools:
                rolls = randint(pool["min_rolls"], pool["max_rolls"])
                pool_items = pool["items"]
                weights = [item[1] for item in pool_items]
                
                selected_items = random.choices(pool_items, weights=weights, k=rolls)
                for item_name, weight, min_amt, max_amt in selected_items:
                    if item_name is None:
                        continue
                        
                    amount, roll_val = loot_num(min_amt, max_amt)
                    if amount > 0:
                        if item_name not in aggregated_drops:
                            aggregated_drops[item_name] = {"amount": 0, "rolls": []}
                        aggregated_drops[item_name]["amount"] += amount
                        aggregated_drops[item_name]["rolls"].append(roll_val)

    elif struct_config.get("use_pools", False):
        min_chests, max_chests = struct_config["chests"]
        num_chests = randint(min_chests, max_chests)
        
        active_pools_to_roll = []

        if "bastion" in selected_structure:
            specific_registry_id = f"{selected_structure.replace(' ', '_')}_pools"
            generic_registry_id = "bastion_generic_pools"

            g_ratio = struct_config.get("generic_ratio", 1)
            s_ratio = struct_config.get("specific_ratio", 1)
            total_ratio_weight = g_ratio + s_ratio

            if total_ratio_weight == 0:
                g_chests = num_chests // 2
                s_chests = num_chests - g_chests
            else:
                g_chests = round((g_ratio / total_ratio_weight) * num_chests)
                s_chests = num_chests - g_chests

                if g_ratio == 0:
                    g_chests, s_chests = 0, num_chests
                elif s_ratio == 0:
                    g_chests, s_chests = num_chests, 0

            for _ in range(g_chests):
                active_pools_to_roll.append(dim_data["loot_pools"][generic_registry_id])
            for _ in range(s_chests):
                active_pools_to_roll.append(dim_data["loot_pools"][specific_registry_id])
        else:
            pool_registry_id = f"{selected_structure.replace(' ', '_')}_pools"
            standard_pools = dim_data["loot_pools"][pool_registry_id]
            for _ in range(num_chests):
                active_pools_to_roll.append(standard_pools)

        for chest_pools in active_pools_to_roll:
            for pool in chest_pools:
                rolls = randint(pool["min_rolls"], pool["max_rolls"])
                pool_items = pool["items"]
                weights = [item[1] for item in pool_items]
                
                selected_items = random.choices(pool_items, weights=weights, k=rolls)
                for item_name, weight, min_amt, max_amt in selected_items:
                    if item_name is None:
                        continue
                        
                    amount, roll_val = loot_num(min_amt, max_amt)
                    if amount > 0:
                        if item_name not in aggregated_drops:
                            aggregated_drops[item_name] = {"amount": 0, "rolls": []}
                        aggregated_drops[item_name]["amount"] += amount
                        aggregated_drops[item_name]["rolls"].append(roll_val)

    else:
        min_chests, max_chests = struct_config["chests"]
        num_chests = randint(min_chests, max_chests)
        pool_id = struct_config["loot_pool"]
        loot_pool_config = dim_data["loot_pools"][pool_id]
        
        for _ in range(num_chests):
            for item_name, min_amt, max_amt in loot_pool_config:
                amount, roll_val = loot_num(min_amt, max_amt)
                if amount > 0:
                    if item_name not in aggregated_drops:
                        aggregated_drops[item_name] = {"amount": 0, "rolls": []}
                    aggregated_drops[item_name]["amount"] += amount
                    aggregated_drops[item_name]["rolls"].append(roll_val)

    if selected_structure == "end city":
        if random.random() < 0.05:
            num_chests += 2
            
            active_pools = dim_data["loot_pools"]["end_city_pools"]
            for _ in range(2):
                for pool in active_pools:
                    rolls = randint(pool["min_rolls"], pool["max_rolls"])
                    pool_items = pool["items"]
                    weights = [item[1] for item in pool_items]
                    
                    selected_items = random.choices(pool_items, weights=weights, k=rolls)
                    for item_name, weight, min_amt, max_amt in selected_items:
                        if item_name is None:
                            continue
                            
                        amount, roll_val = loot_num(min_amt, max_amt)
                        if amount > 0:
                            if item_name not in aggregated_drops:
                                aggregated_drops[item_name] = {"amount": 0, "rolls": []}
                            aggregated_drops[item_name]["amount"] += amount
                            aggregated_drops[item_name]["rolls"].append(roll_val)
            
            ship_static_loot = [
                ("Health Potion", 2),
                ("Elytra", 1)
            ]
            
            if random.random() < 0.8:
                ship_static_loot.append(("Dragon Head", 1))
                
            for item_name, qty in ship_static_loot:
                if item_name not in aggregated_drops:
                    aggregated_drops[item_name] = {"amount": 0, "rolls": []}
                aggregated_drops[item_name]["amount"] += qty
                aggregated_drops[item_name]["rolls"].append(randint(10, 999))
                
            selected_structure = "end city with an accompanying end ship"

    final_drops = []
    for name, data in aggregated_drops.items():
        final_drops.append((name, data["amount"], data["rolls"][-1]))

    return {
        "biome": selected_biome,
        "structure": selected_structure,
        "chests": num_chests,
        "drops": final_drops,
        "discovered": list(set(discovered_names))
    }

class Adventure(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.shared_cooldown = commands.CooldownMapping.from_cooldown(1, 60, commands.BucketType.user)

    async def cog_before_invoke(self, ctx: commands.Context):
        if ctx.command == self.adventure: 
            return

        bucket = self.shared_cooldown.get_bucket(ctx.message)
        retry_after = bucket.update_rate_limit()
        
        if retry_after:
            bucket._tokens = 0
            
            remaining_time = round(retry_after, 1)
            embed = discord.Embed(
                title="Adventure Cooldown",
                description=f"You are exhausted from your last journey! Please rest for another {remaining_time} seconds before adventuring again.",
                color=discord.Color.red(),
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text=f"Shard #{ctx.guild.shard_id + 1}")
            
            await ctx.send(embed=embed)
            
            raise commands.CheckFailure("User is currently on an active adventure cooldown.")

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandInvokeError):
            error = error.original

        if isinstance(error, commands.CheckFailure):
            return
        raise error

    @commands.group(invoke_without_command=True, aliases=["adv"])
    async def adventure(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Adventures",
            description="Go on an adventure and explore different structures for precious loot!",
            color=discord.Color(0x333333),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.add_field(
            name="Dimensions",
            value="`m!adventure overworld` - Explore the Overworld for its structures.\n"
                  "`m!adventure nether` - Explore the Nether for its unique structures.\n"
                  "`m!adventure end` - Explore the barren End for in hopes of finding treasure.\n\n"
                  "You can also specify biomes or structures to explore, as shown below.",
            inline=False
        )
        embed.add_field(
            name="Overworld Adventures",
            value="`m!adventure desert` - Explore the desert biome for desert pyramids.\n"
                  "`m!adventure jungle` - Explore the jungle biome for jungle pyramids.\n"
                  "`m!adventure ocean` - Explore the vast oceans for shipwrecks.",
            inline=False
        )
        embed.add_field(
            name="Nether Adventures",
            value="`m!adventure crimson` - Explore the crimson forest.\n"
                  "`m!adventure warped` - Explore the warped forest.\n"
                  "`m!adventure soulsand` - Explore the soul sand valley.\n"
                  "`m!adventure basalt` - Explore the basalt deltas.",
            inline=False
        )
        embed.add_field(
            name="End Adventures",
            value="`m!adventure endcity` - Explore mysterious end cities for loot.",
            inline=False
        )
        embed.add_field(
            name="Feedback",
            value="Adventures are still in development. If you have suggestions, please join the support server.",
            inline=False
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        embed.set_footer(text=f"Adventures are a work in progress. · Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @adventure.command(aliases=["o", "ow"])
    async def overworld(self, ctx: commands.Context):
        result = run_adventure_action("overworld")
        await self._send_adventure_result(ctx, result, discord.Color(0x228b22))

    @adventure.command(aliases=["desert", "d"])
    async def desert_biome(self, ctx: commands.Context):
        result = run_adventure_action("overworld", "desert")
        await self._send_adventure_result(ctx, result, discord.Color(0xe4d96f))

    @adventure.command(aliases=["jungle", "j"])
    async def jungle_biome(self, ctx: commands.Context):
        result = run_adventure_action("overworld", "jungle")
        await self._send_adventure_result(ctx, result, discord.Color(0x228b22))

    @adventure.command(aliases=["ocean", "oc"])
    async def ocean_biome(self, ctx: commands.Context):
        result = run_adventure_action("overworld", "ocean")
        await self._send_adventure_result(ctx, result, discord.Color(0x008080))

    @adventure.command(aliases=["n"])
    async def nether(self, ctx: commands.Context):
        result = run_adventure_action("nether")
        await self._send_adventure_result(ctx, result, discord.Color(0xff4500))

    @adventure.command(aliases=["nw"])
    async def netherwastes(self, ctx: commands.Context):
        result = run_adventure_action("nether", "netherwastes")
        await self._send_adventure_result(ctx, result, discord.Color(0x8b0000))

    @adventure.command(aliases=["cf", "crimsonforest"])
    async def crimson(self, ctx: commands.Context):
        result = run_adventure_action("nether", "crimson")
        await self._send_adventure_result(ctx, result, discord.Color(0xb22222))

    @adventure.command(aliases=["wf", "warpedforest"])
    async def warped(self, ctx: commands.Context):
        result = run_adventure_action("nether", "warped")
        await self._send_adventure_result(ctx, result, discord.Color(0x008b8b))

    @adventure.command(aliases=["ss", "ssv", "soulsandvalley"])
    async def soulsand(self, ctx: commands.Context):
        result = run_adventure_action("nether", "soulsand")
        await self._send_adventure_result(ctx, result, discord.Color(0x4a3b32))

    @adventure.command(aliases=["bd", "basaltdeltas"])
    async def basalt(self, ctx: commands.Context):
        result = run_adventure_action("nether", "basalt")
        await self._send_adventure_result(ctx, result, discord.Color(0x696969))

    @adventure.command(aliases=["e"])
    async def end(self, ctx: commands.Context):
        result = run_adventure_action("end")
        await self._send_adventure_result(ctx, result, discord.Color(0x9370db))

    @adventure.command(aliases=["endcity", "ec"])
    async def end_city(self, ctx: commands.Context):
        result = run_adventure_action("end", "end city")
        await self._send_adventure_result(ctx, result, discord.Color(0x9370db))

    async def _send_adventure_result(self, ctx: commands.Context, result: dict, embed_color: discord.Color):
        if "error" in result:
            return await ctx.send(result["error"])

        discovery_text = f"You journeyed into a {result['biome']} biome.\n"
        if result["discovered"]:
            if len(result["discovered"]) > 1:
                discovered_str = ", ".join([f"a {s}" for s in result["discovered"]])
                discovery_text += f"**Lucky Find!** On your journey, you spotted signs of multiple structures: {discovered_str}!\n\n"
            else:
                discovery_text += f"On your journey, you spotted signs of a {result['discovered'][0]}.\n\n"
        else:
            discovery_text += "\n\n"

        if result["structure"] == "none":
            adv_desc = (
                f"{discovery_text}"
                "You spent hours wandering through the endless landscape but couldn't safely track down any structures!\n"
                "You return empty-handed this time.\n"
                "Number of Chests: 0"
            )
        else:
            loot_lines = []
            for name, amt, roll_val in result["drops"]:
                loot_lines.append(f"- {name} x{amt} ({roll_val})")

            action_phrase = "decided to advance into" if len(result["discovered"]) > 1 else "ventured out to"
            
            adv_desc = (
                f"{discovery_text}"
                f"You {action_phrase} the {result['structure']} for your adventure!\n\n"
                f"You obtained:-\n" + "\n".join(loot_lines) +
                f"\n\nNumber of Chests: {result['chests']}"
            )

        embed = discord.Embed(
            title="Adventure Log",
            description=adv_desc,
            color=embed_color if result["structure"] != "none" else discord.Color.red(),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        embed.set_footer(text=f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Adventure(bot))