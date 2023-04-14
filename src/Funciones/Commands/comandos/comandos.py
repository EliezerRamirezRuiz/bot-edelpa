from discord.ext import commands

from Funciones.Database.Clases.alerta import Alerta
from Funciones.Database.Clases.robot import Robot
from Funciones.Database.Clases.stock import Stock
from Funciones.Database.Clases.reporte import Reporte

alertas = Alerta()
estado_robot =  Robot()
obtener_stock = Stock()
reporte_dia = Reporte()


class PrincipalCommands(commands.Cog):
    """instancia del bot para controlar los comandos de manera escalable"""
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def consultar_stock(self, ctx):
        """Funcion que consultar stock a pedir, manda mensaje para que el usuario sepa 
        que debe mandar una respuesta para consultar el stock"""

        try:
     
            await ctx.send("Porfavor escriba el codigo del stock a consultar:")        
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
            result = await obtener_stock.get_data(str(message.content))

            await ctx.send(result) 
            
        except Exception as ex:
            await ctx.send(ex)


    @commands.command()
    async def estado_robot(self, ctx):
        """Function para obtener estado del robot"""

        try:
            await ctx.send("Consultando estado del robot")
            result = await estado_robot.get_data()
            await ctx.send(result)

        except Exception as ex:
            await ctx.send(ex)

    
    @commands.command()
    async def ultimas_alertas(self, ctx):
        """Funcion que consulta la funcion `Alerta.ultimas_alertas_activas()` y obtiene el objeto Embed y
            lo retornamos. """

        try:
            await ctx.send("Obteniendo alertas")
            alerta = await alertas.ultimas_alertas_activas()
            await ctx.send(embed=alerta)
            
        except Exception as ex:
            await ctx.send(ex)