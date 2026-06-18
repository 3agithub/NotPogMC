import datetime
import discord
from discord.ext import commands

class CustomHelpClass(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed=discord.Embed(
            title="NotPogMC Help",
            description="All NotPogMC commands are shown below.", color=discord.Color(0xfff5d1),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.add_field(
            name="Help commands",
            value=f"`m!help` - This page.\n\
                `m!info` - Information about the bot.",
            inline=False
        )
        embed.add_field(
            name="Gameplay commands",
            value=f"`m!mine` - Venture into the deep caves for resources.\n\
                `m!chop` - Head to the vast forests and chop for wood.",
            inline=False
        )
        embed.add_field(
            name="Technical commands",
            value=f"`m!ping` / `m!pong` - Check the bot latency.",
            inline=False
        )
        embed.add_field(
            name="Tip: Join our support server!",
            value=f"https://discord.gg/z4AVuyKsyc (Verification is needed)",
            inline=False
        )
        await self.get_destination().send(embed=embed)

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = CustomHelpClass()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))