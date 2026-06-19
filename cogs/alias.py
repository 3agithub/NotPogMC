import datetime
import discord
from discord import app_commands
from discord.ext import commands

class Alias(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, aliases=["a", "aliases"])
    async def alias(self, ctx: commands.Context):
        embed=discord.Embed(
            title="NotPogMC Command Aliases",
            description="The following is a list of all aliases for commands.",
            color=discord.Color(0xfff5d1),
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
            name="Other commands",
            value=f"`m!ping` - `m!pi`\n\
                    `m!pong` - `m!po`\n\
                    `m!credits` - `m!cre`",
            inline=True
        )
        embed.add_field(
            name="Tip:",
            value=f"You can use `m!alias <command>` to view aliases for subcommands of a specific command.",
            inline=False
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text=f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @alias.command(aliases=["m"])
    async def mine(self, ctx: commands.Context):
        embed=discord.Embed(
            title="NotPogMC Command Aliases · m!mine",
            description="`m!mine` - `m!m`",
            color=discord.Color(0xfff5d1),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.add_field(
            name="Subcommands",
            value=f"`m!mine overworld` - `m!m o`, `m!m ow`\n\
                    `m!mine nether` - `m!m n`\n\
                    `m!mine end` - `m!m e`",
            inline=True
        )
        embed.add_field(
            name="Other commands",
            value=f"`m!alias mine` - `m!a m`, `m!aliases m`",
            inline=True
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text=f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @alias.command(aliases=["c"])
    async def mine(self, ctx: commands.Context):
        embed=discord.Embed(
            title="NotPogMC Command Aliases · m!chop",
            description="`m!chop` - `m!c`",
            color=discord.Color(0xfff5d1),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.add_field(
            name="Subcommands",
            value=f"`m!chop overworld` - `m!c o`, `m!c ow`\n\
                    `m!chop nether` - `m!c n`\n\
                    `m!chop end` - `m!c e`",
            inline=True
        )
        embed.add_field(
            name="Other commands",
            value=f"`m!alias chop` - `m!a c`, `m!aliases c`",
            inline=True
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text=f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)
    
    @alias.command(aliases=["adv"])
    async def mine(self, ctx: commands.Context):
        embed=discord.Embed(
            title="NotPogMC Command Aliases · m!adventure",
            description="`m!mine` - `m!adv`",
            color=discord.Color(0xfff5d1),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.add_field(
            name="Subcommands · Dimensional Adventures",
            value=f"`m!adventure overworld` - `m!adv o`, `m!adv ow`\n\
                    `m!adventure nether` - `m!adv n`\n\
                    `m!adventure end` - `m!adv e`",
            inline=True
        )
        embed.add_field(
            name="Subcommands · Biome Adventures (Overworld)",
            value=f"`m!adventure desert` - `m!adv d`\n\
                    `m!adventure jungle` - `m!adv j`\n\
                    `m!adventure ocean` - `m!adv oc`",
            inline=True
        )
        embed.add_field(
            name="Subcommands · Biome Adventures (Nether)",
            value=f"`m!adventure netherwastes` - `m!adv nw`\n\
                    `m!adventure crimson` - `m!adv cf`, `m!adv crimsonforest`\n\
                    `m!adventure warped` - `m!adv wf`, `m!adv warpedforest`\n\
                    `m!adventure soulsand` - `m!adv ss`, `m!adv ssv`, `m!adv soulsandvalley`\n\
                    `m!adventure basalt` - `m!adv bd`, `m!adv basaltdeltas`",
            inline=True
        )
        embed.add_field(
            name="Other commands",
            value=f"`m!alias adventure` - `m!a adv`, `m!aliases adv`",
            inline=True
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text=f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Alias(bot))

