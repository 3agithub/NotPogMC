import datetime
import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["pi"])
    async def ping(self, ctx: commands.Context):
        bot_ping = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="Pong!",
            description=f"Latency: {bot_ping}ms",
            color=discord.Color(0x00ff00),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["po"])
    async def pong(self, ctx: commands.Context):
        bot_ping = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="Ping!",
            description=f"Latency: {bot_ping}ms",
            color=discord.Color(0x00ff00),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))

