from discord.ext import commands
from Functions.Database.Functions.functions_db import obtener_stock, estado_del_robot, obtener_alerta


class PrincipalCommands(commands.Cog):
    """instancia del bot para controlar los comandos de manera escalable"""
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def consultar_stock(self, ctx):
        """Funcion que consultar stock a pedir"""

        try:
            await ctx.send("Porfavor escriba el codigo del stock a consultar:")

            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
            result = await obtener_stock(str(message.content), ctx)

            await ctx.send(result)
            
        except TimeoutError:
            return f"Lo siento se excedio el tiempo para responder, por favor reescriba !consultar_stock"


    @commands.command()
    async def estado_robot(self, ctx):
        """Function para obtener estado del robot"""

        try:
            await ctx.send("Consultando estado del robot")

            result = await estado_del_robot(ctx)
            await ctx.send(result)

        except TimeoutError as error:
            await ctx.send(f"Lo siento se excedio el tiempo para responder, reintente con !menu")

    
    @commands.command()
    async def ultimas_alertas(self, ctx):
        """Funcion que consultar ultimas 5 o 10 alertas"""

        try:
            await ctx.send("Obteniendo alertas")
            
            result = await obtener_alerta()

            await ctx.send('')
            
        except TimeoutError:
            return f"Lo siento se excedio el tiempo para responder, por favor reescriba !consultar_stock"