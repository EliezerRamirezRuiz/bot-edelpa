from discord.ext import commands

from Functions.Database.Funciones.alertas import LeerAlerta
from Functions.Database.Funciones.estado_robot import EstadoRobot
from Functions.Database.Funciones.obtener_stock import ObtenerStock
from Functions.Database.Funciones.reporte_dia import ReporteDia

alertas = LeerAlerta()
estado_robot =  EstadoRobot()
obtener_stock = ObtenerStock()
reporte_dia = ReporteDia()


class PrincipalCommands(commands.Cog):
    """instancia del bot para controlar los comandos de manera escalable"""
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def consultar_stock(self, ctx):
        """Funcion que consultar stock a pedir"""

        try:
            """manda mensaje primero cuando se marca la opcion y despues se invoca este"""
            await ctx.send("Porfavor escriba el codigo del stock a consultar:")
            
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
            result = await obtener_stock.query(str(message.content))

            await ctx.send(result) 
            
        except Exception as ex:
            await ctx.send(ex)


    @commands.command()
    async def estado_robot(self, ctx):
        """Function para obtener estado del robot"""

        try:
            await ctx.send("Consultando estado del robot")

            result = await estado_robot.query()
            await ctx.send(result)

        except Exception as ex:
            await ctx.send(ex)

    
    @commands.command()
    async def ultimas_alertas(self, ctx):
        """Funcion que consultar ultimas 5 o 10 alertas"""

        try:
            await ctx.send("Obteniendo alertas")
            result = await alertas.query()

            await ctx.send(result)
            
        except Exception as ex:
            await ctx.send(ex)