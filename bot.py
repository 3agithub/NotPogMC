import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "m!", \
                    intents = intents, \
                    activity = discord.Activity(type=discord.ActivityType.listening, name="m!help"), \
                    status = discord.Status.do_not_disturb)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(aliases=["sl"])
@commands.is_owner()
async def slash(ctx, action: str, scope: str = "global"):
    if action == "sync":
        await ctx.send(f"Syncing {scope} application commands... please wait.")
        try:
            if scope == "global": synced = await bot.tree.sync()
            elif scope == "guild": synced = await bot.tree.sync(guild=ctx.guild)
            else: return await ctx.send("Invalid scope. Use `global` or `guild`.")
            await ctx.send(f"Successfully synced {len(synced)} {scope} slash command(s).") 
        except Exception as e: await ctx.send(f"Failed to sync commands: {e}")
    elif action == "clear":
        try:
            if scope == "global":
                bot.tree.clear_commands(guild=None)
                await bot.tree.sync()
                await ctx.send("Global slash commands unregistered!")
            elif scope == "guild":
                bot.mtree.clear_commands(guild=ctx.guild)
                await bot.tree.sync(guild=ctx.guild)
                await ctx.send("Guild-specific slash commands unregistered!")
            else: await ctx.send("Invalid scope specified. Use `global` or `guild`.")
        except Exception as e: await ctx.send(f"Failed to clear commands: {e}")   
    else: await ctx.send("Invalid action specified. Use `sync` or `clear`.")

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

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            print(f"Loading extension {filename}...")
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.getenv('BOT_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())