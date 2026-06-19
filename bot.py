import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path
import aiosqlite

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

intents = discord.Intents.all()

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix = "m!",
            intents = intents,
            activity = discord.Activity(type=discord.ActivityType.listening, name="m!help"),
            status = discord.Status.do_not_disturb
        )
        self.db = None

    async def setup_hook(self):
        self.db = await aiosqlite.connect("inventory.db")
        
        async with self.db.cursor() as cursor:
            await cursor.execute("""
                CREATE TABLE IF NOT EXISTS Inventory (
                    user_id INTEGER,
                    item_id INTEGER,
                    quantity INTEGER DEFAULT 0,
                    PRIMARY KEY (user_id, item_id)
                )
            """)
        await self.db.commit()
        print("Databases initialized.")

        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                print(f"Loading extension {filename}...")
                await self.load_extension(f"cogs.{filename[:-3]}")

    async def close(self):
        if self.db:
            await self.db.close()
        await super().close()

bot = Bot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}. Total shards: {bot.shard_count}")

@bot.command(aliases=["lo"])
@commands.is_owner()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension}.")

@bot.command(aliases=["ul"])
@commands.is_owner()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension}.")

@bot.command(aliases=["rl"])
@commands.is_owner()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}.")

async def main():
    async with bot:
        await bot.start(os.getenv('BOT_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())