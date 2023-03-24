from discord.ext import commands
from discord.ui import View, Select
import discord 

class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Menu(self, ctx):
        select = Select(
            placeholder="Quick Options",
            min_values=1,
            max_values=2,
            options=[
                discord.SelectOption(
                label="Option 1",
                description="description option 1",
                default=True,
                value="Option 1"
                ),
                discord.SelectOption(
                label="Option 2",
                description="description option 2",
                value="Option 2"
                ),
            ]
        )
        async def my_callback(interaction):
            if select.values[0] == select.options[0].__getattribute__("label"):
                await interaction.response.send_message(f"option: {select.values[0]}")
            else:    
                await interaction.response.send_message(f"option: {select.values[0]}")

        select.callback = my_callback

        view = View(timeout=10)
        view.add_item(select)
        
        await ctx.send(f'{select.placeholder}', view=view)
    
