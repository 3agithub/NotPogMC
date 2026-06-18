import datetime
import discord
from discord import app_commands
from discord.ext import commands
from random import randint

LOOT_TABLES = {
    "overworld": {
        "biomes": {
            "forest": {"weight": 30, "trees": ["oak", "birch"]},
            "taiga": {"weight": 20, "trees": ["spruce"]},
            "birch forest": {"weight": 10, "trees": ["birch"]},
            "dark forest": {"weight": 10, "trees": ["dark_oak"]},
            "jungle": {"weight": 3, "trees": ["jungle"]},
            "savanna": {"weight": 2, "trees": ["acacia"]},
            "mangrove swamp": {"weight": 7, "trees": ["mangrove"]},
            "cherry grove": {"weight": 10, "trees": ["cherry"]},
            "pale garden": {"weight": 8, "trees": ["pale_oak"]}
        },
        "tree_data": {
            "oak": {"drops": [("Oak Log", 12, 28), ("Oak Sapling", 1, 3), ("Apple", 0, 2), ("Stick", 1, 4)]},
            "spruce": {"drops": [("Spruce Log", 16, 54), ("Spruce Sapling", 2, 5), ("Stick", 1, 5)]},
            "birch": {"drops": [("Birch Log", 10, 16), ("Birch Sapling", 1, 2), ("Stick", 1, 3)]},
            "dark_oak": {"drops": [("Dark Oak Log", 24, 48), ("Dark Oak Sapling", 2, 4), ("Apple", 0, 3), ("Stick", 2, 6)]},
            "jungle": {"drops": [("Jungle Log", 15, 64), ("Jungle Sapling", 1, 3), ("Vines", 0, 4), ("Cocoa Beans", 0, 3)]},
            "acacia": {"drops": [("Acacia Log", 8, 14), ("Acacia Sapling", 1, 2), ("Stick", 1, 3)]},
            "cherry": {"drops": [("Cherry Log", 12, 24), ("Cherry Sapling", 1, 3), ("Pink Petals", 1, 4), ("Stick", 1, 3)]},
            "pale_oak": {"drops": [("Pale Oak Log", 15, 36), ("Pale Oak Sapling", 1, 3), ("Pale Hanging Moss", 1, 4), ("Creaking Heart", 0, 1)]},
            "mangrove": {"drops": [("Mangrove Log", 12, 32), ("Mangrove Propagule", 1, 3), ("Mangrove Roots", 4, 12), ("Muddy Mangrove Roots", 2, 6)]}
        }
    },
    "nether": {
        "biomes": {
            "crimson forest": {"weight": 50, "trees": ["crimson"]},
            "warped forest": {"weight": 50, "trees": ["warped"]}
        },
        "tree_data": {
            "crimson": {"drops": [("Crimson Stem", 14, 32), ("Crimson Fungi", 1, 2), ("Shroomlight", 0, 2), ("Weeping Vines", 0, 3)]},
            "warped": {"drops": [("Warped Stem", 14, 32), ("Warped Fungi", 1, 2), ("Shroomlight", 0, 2), ("Twisting Vines", 0, 3)]}
        }
    },
    "end": {
        "biomes": {
            "end highlands": {"weight": 100, "trees": ["chorus_plant"]}
        },
        "tree_data": {
            "chorus_plant": {"drops": [("Chorus Fruit", 10, 24), ("Chorus Flower", 1, 3)]}
        }
    }
}

def loot_num(min_val, max_val):
    res = randint(0, 1000)
    final_amt = round(res / 1000 * (max_val - min_val) + min_val)
    return [final_amt, res]

def run_chop_action(dimension: str) -> dict:
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

    @commands.group(invoke_without_command=True)
    async def chop(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Chopping",
            description=f"Explore different dimensions and chop for resources!\nOverworld: `m!chop overworld`\nNether: `m!chop nether`\nEnd: `m!chop end`",
            color=discord.Color(0x333333),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        await ctx.send(embed=embed)

    @chop.command()
    async def overworld(self, ctx: commands.Context):
        result = run_chop_action("overworld")
        if "error" in result:
            return await ctx.send(result["error"])

        loot_lines = []
        for name, amt, roll_val in result["drops"]:
            loot_lines.append(f"- {name} ×{amt} ({roll_val})")

        ow_desc = (
            f"You venture into the Overworld, searching through a {result['biome']}. "
            f"You chop for precious wood and resources while avoiding dangerous monsters lurking in the shadows.\n\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="Overworld Chopping",
            description=ow_desc,
            color=discord.Color(0x228b22),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        await ctx.send(embed=embed)
    
    @chop.command()
    async def nether(self, ctx: commands.Context):
        result = run_chop_action("nether")
        if "error" in result:
            return await ctx.send(result["error"])

        loot_lines = []
        for name, amt, roll_val in result["drops"]:
            loot_lines.append(f"- {name} ×{amt} ({roll_val})")

        nether_desc = (
            f"You step into the fiery Nether, arriving inside a dense {result['biome']}. "
            f"You chop for valuable resources while trying to avoid getting burned alive.\n\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="Nether Chopping",
            description=nether_desc,
            color=discord.Color(0xff4500),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        await ctx.send(embed=embed)

    @chop.command()
    async def end(self, ctx: commands.Context):
        result = run_chop_action("end")
        if "error" in result:
            return await ctx.send(result["error"])

        loot_lines = []
        for name, amt, roll_val in result["drops"]:
            loot_lines.append(f"- {name} ×{amt} ({roll_val})")

        end_desc = (
            f"You rift into the cold void of the End and travel out to the {result['biome']}. "
            f"You harvest exotic stalks while monitoring your step over the endless starry abyss.\n\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="End Chopping",
            description=end_desc,
            color=discord.Color(0x9370db),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        await ctx.send(embed=embed)
 
async def setup(bot: commands.Bot):
    await bot.add_cog(Chop(bot))