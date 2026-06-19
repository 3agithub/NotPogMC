import datetime
import discord
from discord.ext import commands

class Cooldown(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["cd"])
    async def cooldown(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Command Cooldowns",
            color=discord.Color(0x36f2ff),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        
        cogs_to_check = {
            "Mining": "Mine",
            "Chopping": "Chop",
            "Adventuring": "Adventure"
        }
        
        for display_name, cog_name in cogs_to_check.items():
            cog_instance = self.bot.get_cog(cog_name)
            status_text = "Ready"
            
            if cog_instance and hasattr(cog_instance, "cooldown"):
                bucket = cog_instance.cooldown.get_bucket(ctx.message)
                
                cd = bucket.get_retry_after()
                if cd > 0:
                    m = int(cd // 60)
                    s = int(cd % 60)
                    
                    if m > 0: status_text = f"Under cooldown · {m}m{s:02d}s"
                    else: status_text = f"Under cooldown · {s}s"
                        
            embed.add_field(
                name=display_name,
                value=f"{status_text}",
                inline=True
            )
            
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
        embed.set_footer(text = f"Shard #{ctx.guild.shard_id + 1}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Cooldown(bot))