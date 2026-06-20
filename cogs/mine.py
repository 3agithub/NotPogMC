import datetime
import discord
from discord import app_commands
from discord.ext import commands
from random import randint
from items import ITEM_REGISTRY
from loot_tables import MINE as LOOT_TABLES
from cogs.inventory import save_player_loot
from configs import MINE_CD

def loot_num(min, max):
    res = randint(0, 1000)
    return [round(res / 1000 * (max - min) + min), res]

class Mine(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cd = MINE_CD
        self.cooldown = commands.CooldownMapping.from_cooldown(1, self.cd, commands.BucketType.user)

    async def cog_before_invoke(self, ctx: commands.Context):
        if ctx.command == self.mine: 
            return

        bucket = self.cooldown.get_bucket(ctx.message)
        current_timestamp = datetime.datetime.now(datetime.timezone.utc).timestamp()
        retry_after = bucket.update_rate_limit(current_timestamp)
        
        if retry_after:
            bucket._tokens = 0
            remaining_time = round(retry_after, 1)
            embed = discord.Embed(
                title="Mining Cooldown",
                description=f"You are exhausted from your last mining expedition! Please rest for another {remaining_time} seconds before digging again.",
                color=discord.Color.red(),
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text=f"Shard #{ctx.guild.shard_id + 1}")
            
            await ctx.send(embed=embed)
            raise commands.CheckFailure("User is currently on an active mining cooldown.")

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandInvokeError):
            error = error.original
        if isinstance(error, commands.CheckFailure):
            return
        raise error

    @commands.group(invoke_without_command=True, aliases=["m"])
    async def mine(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Mining",
            description=f"Explore different dimensions and mine for resources! ({self.cd}s cooldown)\n\
                          Overworld: `m!mine overworld`\n\
                          Nether: `m!mine nether`\n\
                          End: `m!mine end`",
            color=discord.Color(0x4a4842),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

    @mine.command(aliases=["o", "ow"])
    async def overworld(self, ctx: commands.Context):
        loot_lines = []
        drops_to_save = []
        
        for item_id, min_val, max_val in LOOT_TABLES["overworld"]:
            amount, roll_val = loot_num(min_val, max_val)
            if amount > 0:
                item_name = ITEM_REGISTRY.get(item_id, f"Unknown (ID: {item_id})")
                loot_lines.append(f"- {item_name} ×{amount} ({roll_val})")
                drops_to_save.append((item_id, amount))


        if drops_to_save:
            await save_player_loot(self.bot.db, ctx.author.id, drops_to_save)

        ow_desc = (
            f"You venture into the Overworld, surrounded by lush forests and towering mountains.\n"
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
        drops_to_save = []
        
        for item_id, min_val, max_val in LOOT_TABLES["nether"]:
            amount, roll_val = loot_num(min_val, max_val)
            if amount > 0:
                item_name = ITEM_REGISTRY.get(item_id, f"Unknown (ID: {item_id})")
                loot_lines.append(f"- {item_name} ×{amount} ({roll_val})")
                drops_to_save.append((item_id, amount))

        if drops_to_save:
            await save_player_loot(self.bot.db, ctx.author.id, drops_to_save)

        nether_desc = (
            f"You descend into the Nether, filled with lava, hot biomes and ancient structures.\n"
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
        drops_to_save = []
        
        for item_id, min_val, max_val in LOOT_TABLES["end"]:
            amount, roll_val = loot_num(min_val, max_val)
            if amount > 0:
                item_name = ITEM_REGISTRY.get(item_id, f"Unknown (ID: {item_id})")
                loot_lines.append(f"- {item_name} ×{amount} ({roll_val})")
                drops_to_save.append((item_id, amount))

        if drops_to_save:
            await save_player_loot(self.bot.db, ctx.author.id, drops_to_save)

        end_desc = (
            f"You travel to the End, filled with nothing more but end stone, chorus plants and end cities.\n\n"
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