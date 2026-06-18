import datetime
import discord
from discord import app_commands
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["i"])
    async def info(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Hello, I'm NotPogMC!",
            description=f"I'm a Minecraft-themed game bot created by <@554984391219347456>, and have been been running since <t:1781675461>.\n\
                I was initially created in February 2022, but shut down in August 2023.\n\n\
                Prefix: `m!`\n\
                For a list of all commands, type `m!help`.\n\n\
                If you have any questions, suggestions, or just want to chat, feel free to join our support server: `https://discord.gg/z4AVuyKsyc (Verification is needed)`",
            color=discord.Color(0x00ff00),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))

