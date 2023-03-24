from discord.ext import commands
from discord.ui import View
from Components.menu_component import Menu


class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Menu(self, ctx):
        select = Menu()

        view = View(timeout=10)
        view.add_item(select)

        await ctx.send(select.placeholder, view=view)


