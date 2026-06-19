import datetime
from math import floor, ceil
import discord
from discord import app_commands
from discord.ext import commands
import aiosqlite
import bisect
from loot_tables import ITEM_REGISTRY

async def save_player_loot(db_connection: aiosqlite.Connection, user_id: int, drops: list):
    if not drops:
        return

    safe_name_to_id = {
        name: item_id for item_id, name in ITEM_REGISTRY.items() 
        if not str(item_id).endswith('00') or item_id == 0
    }

    async with db_connection.cursor() as cursor:
        for item_data in drops:
            item_name = item_data[0]
            quantity = item_data[1]
            
            item_id = safe_name_to_id.get(item_name)
            
            if item_id is None:
                print(f"Warning: Attempted to save unregistered item '{item_name}'")
                continue
                
            await cursor.execute("""
                INSERT INTO Inventory (user_id, item_id, quantity)
                VALUES (?, ?, ?)
                ON CONFLICT(user_id, item_id) 
                DO UPDATE SET quantity = quantity + excluded.quantity
            """, (user_id, item_id, quantity))
            
        await db_connection.commit()


class Paginator(discord.ui.View):
    def __init__(self, author: discord.User, rows: list, shard_text: str, cog):
        super().__init__(timeout=60.0)
        self.author = author
        self.rows = rows
        self.shard_text = shard_text
        self.cog = cog
        self.current_page = 0
        self.max_items_per_page = 9
        self.view_mode = "Categories"
        self.sort_criterion = "ID"
        self.sort_direction = "DESC"
        self.quantity_display = "Stacks"
        self.message = None
        
        self.process_data()
        self.update_buttons()

    def format_quantity(self, item_name, quantity):
        if self.quantity_display == "Raw":
            return f"{item_name} [×{quantity}]"
        if quantity >= 64:
            return f"{item_name} [×{floor(quantity/64)}s{quantity%64:02d}]"
        return f"{item_name} [×{quantity}]"

    def process_data(self):
        if self.view_mode == "Categories":
            self.max_items_per_page = 9
            raw_categories = {}
            for item_id, quantity in self.rows:
                if str(item_id).endswith('00') and item_id != 0:
                    continue

                category_name, header_id = self.cog._get_item_category_details(item_id)
                item_name = ITEM_REGISTRY.get(item_id, f"Unknown Item (ID: {item_id})")
                
                item_line = self.format_quantity(item_name, quantity)

                item_entry = {
                    "id": item_id,

                    "quantity": quantity,
                    "line": item_line
                }

                if category_name not in raw_categories:
                    raw_categories[category_name] = {
                        "header_id": header_id,
                        "total_qty": 0,
                        "items": []
                    }
                
                raw_categories[category_name]["items"].append(item_entry)
                raw_categories[category_name]["total_qty"] += quantity

            self.categorized_data = {}
            if self.sort_criterion == "ID":
                self.categories = sorted(raw_categories.keys(), key=lambda c: raw_categories[c]["header_id"])
                for cat in self.categories:
                    self.categorized_data[cat] = sorted(raw_categories[cat]["items"], key=lambda i: i["id"])
            else:
                is_reverse = (self.sort_direction == "DESC")
                self.categories = sorted(raw_categories.keys(), key=lambda c: raw_categories[c]["total_qty"], reverse=is_reverse)
                for cat in self.categories:
                    self.categorized_data[cat] = sorted(raw_categories[cat]["items"], key=lambda i: i["quantity"], reverse=is_reverse)
            
            self.total_pages = max(1, ceil(len(self.categories) / self.max_items_per_page))

        else:
            self.max_items_per_page = 45
            self.flat_items = []
            for item_id, quantity in self.rows:
                if str(item_id).endswith('00') and item_id != 0:
                    continue

                item_name = ITEM_REGISTRY.get(item_id, f"Unknown Item (ID: {item_id})")
                item_line = self.format_quantity(item_name, quantity)

                self.flat_items.append({
                    "id": item_id,
                    "quantity": quantity,
                    "line": item_line
                })

            if self.sort_criterion == "ID":
                self.flat_items = sorted(self.flat_items, key=lambda i: i["id"])
            else:
                is_reverse = (self.sort_direction == "DESC")
                self.flat_items = sorted(self.flat_items, key=lambda i: i["quantity"], reverse=is_reverse)

            self.total_pages = max(1, ceil(len(self.flat_items) / self.max_items_per_page))

        if self.current_page >= self.total_pages:
            self.current_page = self.total_pages - 1

    def update_buttons(self):
        self.prev_page_button.disabled = (self.current_page == 0)
        self.next_page_button.disabled = (self.current_page >= self.total_pages - 1)
        
        self.toggle_view_button.label = f"View: {self.view_mode}"
        self.toggle_criterion_button.label = f"Sort: {self.sort_criterion}"
        self.toggle_qty_button.label = f"Quantity Format: {self.quantity_display}"
        
        if self.sort_criterion == "Amount":
            self.toggle_direction_button.disabled = False
            self.toggle_direction_button.label = f"Order: {self.sort_direction}"
        else:
            self.toggle_direction_button.disabled = True
            self.toggle_direction_button.label = "Order: N/A"

    def create_page_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title=f"Your Inventory",
            color=discord.Color(0xb57104),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name=self.author.name, icon_url=self.author.display_avatar.url)
        
        if self.view_mode == "Categories":
            start_idx = self.current_page * self.max_items_per_page
            end_idx = start_idx + self.max_items_per_page
            page_categories = self.categories[start_idx:end_idx]

            for category in page_categories:
                items_list = self.categorized_data[category]
                field_value = "\n".join([item["line"] for item in items_list])
                
                if len(field_value) > 1024:
                    field_value = field_value[:1020] + "..."
                    
                embed.add_field(name=category, value=field_value, inline=True)
        else:
            start_idx = self.current_page * self.max_items_per_page
            end_idx = start_idx + self.max_items_per_page
            page_items = self.flat_items[start_idx:end_idx]
            
            lines = [item["line"] for item in page_items]
            
            col_size = 15
            for i in range(0, len(lines), col_size):
                col_lines = lines[i:i + col_size]
                field_value = "\n".join(col_lines)
                if len(field_value) > 1024:
                    field_value = field_value[:1020] + "..."
                if i == 0: title = "List of Items"
                else: title = "\u200b"
                embed.add_field(name=title, value=field_value, inline=True)

        embed.set_footer(text=f"Page {self.current_page + 1}/{self.total_pages} · {self.shard_text}")
        return embed

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author.id:
            await interaction.response.send_message("This is not your inventory.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="Previous", style=discord.ButtonStyle.blurple, row=0)
    async def prev_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_buttons()
            await interaction.response.edit_message(embed=self.create_page_embed(), view=self)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.blurple, row=0)
    async def next_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_buttons()
            await interaction.response.edit_message(embed=self.create_page_embed(), view=self)

    @discord.ui.button(label="View: Categories", style=discord.ButtonStyle.gray, row=1)
    async def toggle_view_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.view_mode == "Categories":
            self.view_mode = "Flat List"
        else:
            self.view_mode = "Categories"
            
        self.process_data()
        self.update_buttons()
        await interaction.response.edit_message(embed=self.create_page_embed(), view=self)

    @discord.ui.button(label="Sort: ID", style=discord.ButtonStyle.gray, row=1)
    async def toggle_criterion_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.sort_criterion == "ID":
            self.sort_criterion = "Amount"
        else:
            self.sort_criterion = "ID"
            
        self.process_data()
        self.update_buttons()
        await interaction.response.edit_message(embed=self.create_page_embed(), view=self)

    @discord.ui.button(label="Order: DESC", style=discord.ButtonStyle.gray, row=1)
    async def toggle_direction_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.sort_direction == "DESC":
            self.sort_direction = "ASC"
        else:
            self.sort_direction = "DESC"
            
        self.process_data()
        self.update_buttons()
        await interaction.response.edit_message(embed=self.create_page_embed(), view=self)

    @discord.ui.button(label="Quantity Format: Stacks", style=discord.ButtonStyle.gray, row=2)
    async def toggle_qty_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.quantity_display == "Stacks":
            self.quantity_display = "Raw"
        else:
            self.quantity_display = "Stacks"
            
        self.process_data()
        self.update_buttons()
        await interaction.response.edit_message(embed=self.create_page_embed(), view=self)

    async def on_timeout(self):
        for item in self.children:
            if isinstance(item, discord.ui.Button):
                item.disabled = True
        try:
            if self.message:
                await self.message.edit(view=self)
        except Exception:
            pass


class Inventory(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._category_ids = sorted([
            k for k in ITEM_REGISTRY.keys() 
            if str(k).endswith('00') or k == 0
        ])

    def _get_item_category_details(self, item_id: int) -> tuple:
        if not self._category_ids:
            return ("Miscellaneous Group", 999999)

        idx = bisect.bisect_right(self._category_ids, item_id)
        if idx > 0:
            matched_header_id = self._category_ids[idx - 1]
            return (ITEM_REGISTRY[matched_header_id], matched_header_id)

        return ("Miscellaneous Group", 999999)

    @commands.command(aliases=["inv"])
    async def inventory(self, ctx: commands.Context):
        if not hasattr(self.bot, 'db') or self.bot.db is None:
            return await ctx.send("Database connection is not ready yet.")

        async with self.bot.db.cursor() as cursor:
            await cursor.execute("""
                SELECT item_id, quantity FROM Inventory 
                WHERE user_id = ? AND quantity > 0
            """, (ctx.author.id,))
            rows = await cursor.fetchall()
        
        if not rows:
            embed = discord.Embed(
                title="Your inventory...",
                description="... is currently empty. Maybe start an activity to get some items?",
                color=discord.Color(0xb57104),
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=embed)
            return

        shard_string = f"Shard #{ctx.guild.shard_id + 1}"

        view = Paginator(
            author=ctx.author, 
            rows=rows, 
            shard_text=shard_string,
            cog=self
        )
        
        initial_embed = view.create_page_embed()
        message = await ctx.send(embed=initial_embed, view=view)
        view.message = message


async def setup(bot: commands.Bot):
    await bot.add_cog(Inventory(bot))
