from discord.ext import commands
from discord.ui import View, Select
import discord 

class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Menu(self, ctx):

        select = Select(
            placeholder="Fast options",
            options=[
                discord.SelectOption(
                label="Welcome",
                description="it's for say you welcome",
                default=True,
                value="hola"
                ),
                discord.SelectOption(
                label="Welcofgbhgftbhfme",
                description="it's for say you wgfbhelcome",
                value="Valdgvsd"
                ),
            ]
        )
        view = View()
        view.add_item(select)
        
        await ctx.send('aaahhhhhhhhhh', view=view)
    
