import datetime
import discord
from discord import app_commands
from discord.ext import commands

class Alias(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["a", "aliases"])
    async def alias(self, ctx: commands.Context):
        embed=discord.Embed(
            title="NotPogMC Command Aliases",
            description="The following is a list of all aliases for commands.", color=discord.Color(0xfff5d1),
            
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.add_field(
            name="Help commands",
            value=f"`m!help` - `m!h`, `m!?`\n\
                    `m!info` - `m!i`\n\
                    `m!alias` - `m!a`, `m!aliases`",
            inline=True
        )
        embed.add_field(
            name="Gameplay commands",
            value=f"`m!mine` - `m!m`\n\
                    `m!chop` - `m!c`\n\
                    `m!adventure` - `m!adv`",
            inline=True
        )
        embed.add_field(
            name="Economy commands",
            value=f"`m!inventory` - `m!inv`",
            inline=True
        )
        embed.add_field(
            name="Technical commands",
            value=f"`m!ping` - `m!pi`\n\
                    `m!pong` - `m!po`",
            inline=True
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text=f"Aliases are still in progress. / means the command does not have an alias.\nThis is not the place to look for help. If you're finding help, please check m!help for all commands and their uses. · Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Alias(bot))

