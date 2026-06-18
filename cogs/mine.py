import datetime
import discord
from discord import app_commands
from discord.ext import commands
from random import randint
from loot_tables import MINE as LOOT_TABLES

def loot_num(min, max):
    res = randint(0, 1000)
    return [res / 1000 * (max - min) + min, res]

class Mine(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, aliases=["m"])
    async def mine(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Mining",
            description=f"Explore different dimensions and mine for resources!\nOverworld: `m!mine overworld`\nNether: `m!mine nether`\nEnd: `m!mine end`",
            color=discord.Color(0x333333),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @mine.command(aliases=["o", "ow"])
    async def overworld(self, ctx: commands.Context):
        loot_lines = []
        for name, min_val, max_val in self.LOOT_TABLES["overworld"]:
            roll = loot_num(min_val, max_val)
            loot_lines.append(f"- {name} ×{roll[0]:.0f} ({roll[1]})")

        ow_desc = (
            f"You venture into the Overworld, surrounded by lush forests and towering mountains. "
            f"You mine for precious minerals, while avoiding dangerous monsters lurking in the shadows.\n\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="Overworld Mining",
            description=ow_desc,
            color=discord.Color(0x228b22),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @mine.command(aliases=["n"])
    async def nether(self, ctx: commands.Context):
        loot_lines = []
        for name, min_val, max_val in self.LOOT_TABLES["nether"]:
            roll = loot_num(min_val, max_val)
            loot_lines.append(f"- {name} ×{roll[0]:.0f} ({roll[1]})")

        nether_desc = (
            f"You descend into the Nether, a hellish realm filled with lava, ghasts, and ancient structures."
            f"You mine for nether quartz and ancient debris, but beware of the dangers that lurk within its biomes.\n\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="Nether Mining",
            description=nether_desc,
            color=discord.Color(0xff4500),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @mine.command(aliases=["e"])
    async def end(self, ctx: commands.Context):
        loot_lines = []
        for name, min_val, max_val in self.LOOT_TABLES["end"]:
            roll = loot_num(min_val, max_val)
            loot_lines.append(f"- {name} ×{roll[0]:.0f} ({roll[1]})")

        end_desc = (
            f"You travel to the End, a barren dimension filled with nothing more but end stone, chorus plants and end cities. "
            f"You mine for the lone resources available here, but be careful not to fall into the void.\n\n"
            f"You obtained:\n" + "\n".join(loot_lines)
        )

        embed = discord.Embed(
            title="End Mining",
            description=end_desc,
            color=discord.Color(0x9370db),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Mine(bot))