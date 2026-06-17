import datetime
import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")

    @commands.command()
    async def pong(self, ctx: commands.Context):
        await ctx.send("Ping!")

    @app_commands.command(name="ping", description="Pong! Shows the current bot latency.")
    async def embed_base(self, interaction: discord.Interaction):
        bot_ping = round(self.bot.latency * 1000)
        
        embed = discord.Embed(
            title="Pong!",
            description=f"Ping: {bot_ping}ms",
            color=discord.Color(0x00ff00),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))

