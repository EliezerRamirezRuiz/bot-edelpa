from discord.ext import commands
from Functions.Database.db import get_stock

class PrincipalCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def consultar_stock(self, ctx):
        """Funcion que consultar stock a pedir"""
        try:
            await ctx.send("Porfavor escriba el codigo del stock a consultar:")

            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
            result = await get_stock(str(message.content), ctx)

            await ctx.send(result)
            
        except TimeoutError:
            return f"Lo siento se excedio el tiempo para responder, por favor reescriba !consultar_stock"


    @commands.command()
    async def estado_robot(self, ctx):
        try:
            await ctx.send("Consultando estado del robot")
            result = ''
            
        except TimeoutError as error:
            await ctx.send(f"Lo siento se excedio el tiempo para responder, reintente con !menu")