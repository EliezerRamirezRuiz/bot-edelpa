from discord.ext import commands
from discord.ui import View
from Functions.Components.menu_component import Menu
from asyncio import TimeoutError

class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self, ctx):
        select = Menu(self.bot, ctx, self)

        view = View(timeout=180)
        view.add_item(select)

        await ctx.send(select.placeholder, view=view)
    

    @commands.command()
    async def consultar_stock(self, ctx):
        try:
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)

            if type(int(message.content)) == int:
                await ctx.send("Trabajando")
            else:
                await ctx.send("El codigo solo contiene numeros")

        except TimeoutError as error:
            await ctx.send(f"Lo siento se excedio el tiempo para responder, reintente con !menu")
        


