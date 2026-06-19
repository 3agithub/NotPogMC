import datetime
import random
import discord
from discord.ext import commands
from configs import DEATH_MESSAGES, DEATH_MOBS, DEATH_ITEMS

class DeathConfirmView(discord.ui.View):
    def __init__(self, author: discord.User, db_connection):
        super().__init__(timeout=30.0)
        self.author = author
        self.db = db_connection
        self.message = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author.id:
            await interaction.response.send_message("This choice is not yours to make.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="Yes, reset me", style=discord.ButtonStyle.danger)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        for item in self.children:
            item.disabled = True
            
        async with self.db.cursor() as cursor:
            await cursor.execute("DELETE FROM Inventory WHERE user_id = ?", (self.author.id,))
        await self.db.commit()

        random_phrase = random.choice(DEATH_MESSAGES)
        random_mob = random.choice(DEATH_MOBS)
        random_item = random.choice(DEATH_ITEMS)

        formatted_message = random_phrase.format(
            name=self.author.name,
            mob=random_mob,
            item=random_item
        )

        embed = discord.Embed(
            title="You Died!",
            description=f"{formatted_message}",
            color=discord.Color(0xba1904),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name=self.author.name, icon_url=self.author.display_avatar.url)
        
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Nevermind", style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        for item in self.children:
            item.disabled = True
            
        embed = discord.Embed(
            title="Death Avoided",
            description="You stepped back from the brink. Your profile remains safe.",
            color=discord.Color.green()
        )
        await interaction.response.edit_message(embed=embed, view=self)

    async def on_timeout(self):
        for item in self.children:
            item.disabled = True
        try:
            if self.message:
                await self.message.edit(view=self)
        except Exception:
            pass


class Die(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["suicide", "die"])
    async def kill(self, ctx: commands.Context):
        if not hasattr(self.bot, 'db') or self.bot.db is None:
            return await ctx.send("Database connection is not ready yet.")

        embed = discord.Embed(
            title="Are you absolutely sure?",
            description="Executing this command will **permanently delete** every single item in your inventory. This action cannot be undone.",
            color=discord.Color.orange()
        )
        
        view = DeathConfirmView(author=ctx.author, db_connection=self.bot.db)
        message = await ctx.send(embed=embed, view=view)
        view.message = message


async def setup(bot: commands.Bot):
    await bot.add_cog(Die(bot))
