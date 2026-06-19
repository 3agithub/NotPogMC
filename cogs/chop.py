import datetime
import discord
from discord import app_commands
from discord.ext import commands
from random import randint
from loot_tables import CHOP as LOOT_TABLES
from cogs.inventory import save_player_loot
from configs import CHOP_CD

def loot_num(min, max):
    res = randint(0, 1000)
    return [round(res / 1000 * (max - min) + min), res]

def run_chop_action(dimension) -> dict:
    dim_data = LOOT_TABLES.get(dimension.lower())
    if not dim_data:
        return {"error": "Invalid dimension specified."}

    biomes = list(dim_data["biomes"].keys())
    weights = [dim_data["biomes"][b]["weight"] for b in biomes]
    
    total_weight = sum(weights)
    roll = randint(1, total_weight)
    
    current_sum = 0
    selected_biome = biomes[0]
    for biome, w in zip(biomes, weights):
        current_sum += w
        if roll <= current_sum:
            selected_biome = biome
            break

    available_trees = dim_data["biomes"][selected_biome]["trees"]
    selected_tree_id = available_trees[randint(0, len(available_trees) - 1)]
    tree_config = dim_data["tree_data"][selected_tree_id]

    final_drops = []
    for item_name, min_amt, max_amt in tree_config["drops"]:
        amount, roll_val = loot_num(min_amt, max_amt)
        if amount > 0:
            final_drops.append((item_name, amount, roll_val))

    return {
        "biome": selected_biome,
        "drops": final_drops
    }


class Chop(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cd = CHOP_CD
        self.cooldown = commands.CooldownMapping.from_cooldown(1, self.cd, commands.BucketType.user)

    async def cog_before_invoke(self, ctx: commands.Context):
        if ctx.command == self.chop: 
            return

        bucket = self.cooldown.get_bucket(ctx.message)
        retry_after = bucket.update_rate_limit()
        
        if retry_after:
            bucket._tokens = 0
            remaining_time = round(retry_after, 1)
            embed = discord.Embed(
                title="Chopping Cooldown",
                description=f"You are exhausted from your last chopping expedition! Please rest for another {remaining_time} seconds before swinging your axe again.",
                color=discord.Color.red(),
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text=f"Shard #{ctx.guild.shard_id + 1}")
            
            await ctx.send(embed=embed)
            raise commands.CheckFailure("User is currently on an active chopping cooldown.")

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandInvokeError):
            error = error.original
        if isinstance(error, commands.CheckFailure):
            return
        raise error

    @commands.group(invoke_without_command=True, aliases=["c"])
    async def chop(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Chopping",
            description=f"Explore different dimensions and chop for resources! ({self.cd}s cooldown)\n\
                          Overworld: `m!chop overworld`\n\
                          Nether: `m!chop nether`\n\
                          End: `m!chop end`",
            color=discord.Color(0x291804),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @chop.command(aliases=["o", "ow"])
    async def overworld(self, ctx: commands.Context):
        result = run_chop_action("overworld")
        if "error" in result:
            return await ctx.send(result["error"])

        if result.get("drops"):
            await save_player_loot(self.bot.db, ctx.author.id, result["drops"])

        loot_lines = []
        for name, amt, roll_val in result["drops"]:
            loot_lines.append(f"- {name} ×{amt} ({roll_val})")

        ow_desc = (
            f"You venture into the Overworld, searching through a {result['biome']}.\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="Overworld Chopping",
            description=ow_desc,
            color=discord.Color(0x228b22),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)
    
    @chop.command(aliases=["n"])
    async def nether(self, ctx: commands.Context):
        result = run_chop_action("nether")
        if "error" in result:
            return await ctx.send(result["error"])
        
        if result.get("drops"):
            await save_player_loot(self.bot.db, ctx.author.id, result["drops"])

        loot_lines = []
        for name, amt, roll_val in result["drops"]:
            loot_lines.append(f"- {name} ×{amt} ({roll_val})")

        nether_desc = (
            f"You step into the fiery Nether, arriving inside a dense {result['biome']}.\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="Nether Chopping",
            description=nether_desc,
            color=discord.Color(0xff4500),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @chop.command(aliases=["e"])
    async def end(self, ctx: commands.Context):
        result = run_chop_action("end")
        if "error" in result:
            return await ctx.send(result["error"])

        if result.get("drops"):
            await save_player_loot(self.bot.db, ctx.author.id, result["drops"])

        loot_lines = []
        for name, amt, roll_val in result["drops"]:
            loot_lines.append(f"- {name} ×{amt} ({roll_val})")

        end_desc = (
            f"You rift into the cold void of the End and travel out to the {result['biome']}.\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="End Harvesting",
            description=end_desc,
            color=discord.Color(0x9370db),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)
 
async def setup(bot: commands.Bot):
    await bot.add_cog(Chop(bot))