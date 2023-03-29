from discord.ext import commands
from discord.ui import View
from Functions.Components.menu_component import Menu
from asyncio import TimeoutError
from Functions.Complements.complements_code import check_int


class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def menu(self, ctx):
        select = Menu(self.bot, ctx, self)
        view = View(timeout=180)
        view.add_item(select)
        await ctx.send(select.placeholder, view=view)
    

    @menu.command()
    async def stock(self, ctx):
        """Funcion que funciona solo si el padre menu lo llama, ademas consultar stock a pedir"""
        try:
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)

            value = check_int(message)
            
            if value:
                print("next code...")
            else:
                print("stop...")
        
        except TimeoutError as error:
            await ctx.send(f"Lo siento se excedio el tiempo para responder, reintente con !menu")


    @commands.command()
    async def consultar_stock(self, ctx):
        """Funcion que consultar stock a pedir"""
        try:
            await ctx.send("Porfavor escriba el codigo del stock a consultar:")
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)

            value = check_int(message)

            if value:
                print("next code...")
            else:
                print("stop...")

        except TimeoutError as error:
            await ctx.send(f"{error.__cause__}\n reintente con !menu")

