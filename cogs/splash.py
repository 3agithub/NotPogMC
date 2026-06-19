import discord
from discord.ext import commands, tasks
import random
from configs import SPLASHES, SPLASH_INTERVAL

class Splash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.old_splash = None
        self.splash_status.start()

    def cog_unload(self):
        self.splash_status.cancel()

    @tasks.loop(seconds=SPLASH_INTERVAL)
    async def splash_status(self):
        if self.old_splash and len(SPLASHES) > 1:
            available_choices = [s for s in SPLASHES if s != self.old_splash]
            splash = random.choice(available_choices)
        else: splash = random.choice(SPLASHES)
        
        self.old_splash = splash 
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"m!help | {splash}"))
        print(f"Status changed, splash now \"{splash}\"")

    @splash_status.before_loop
    async def before_splash_status(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Splash(bot))
