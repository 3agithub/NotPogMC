import datetime
import discord
from discord import app_commands
from discord.ext import commands

class Credits(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["cre"])
    async def credits(self, ctx: commands.Context):
        embed = discord.Embed(
            title="★ Credits ★",
            description=f"NotPogMC was the group effort of all the following people. Without any of them, this bot would not be possible.",
            color=discord.Color(0xffff00),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.add_field(
            name="Creator & Main Dev",
            value="<@554984391219347456>",
            inline=False
        )
        embed.add_field(
            name="Developer Team",
            value="<@554984391219347456> · <@628917190724288512>",
            inline=False)
        embed.add_field(
            name="Credits for NotPogMC (2022-2023 version)",
            value="**Developer Team**\n<@554984391219347456> · <@430906248272150549> · <@734663076279877633>\n\
                   **Suggestions Team**\n<@734663076279877633> · <@628917190724288512>",
            inline=False
        )
        embed.add_field(
            name="You, the player",
            value="Without you, this bot would not be possible. Thank you for playing!",
            inline=False
        )
        embed.set_thumbnail(url="https://minecraft.wiki/images/Gold_Ingot_JE4_BE2.png")
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Credits(bot))