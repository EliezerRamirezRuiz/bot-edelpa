from discord.ext import commands
from discord.ui import View
from Components.menu_component import Menu
import asyncio

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
        await ctx.send("Por favor envíe su mensaje:")
        try:
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
            print(message.content)
            await ctx.send("good")
        except asyncio.TimeoutError:
            await ctx.send("Lo siento, el tiempo para enviar un mensaje ha expirado.")
        


