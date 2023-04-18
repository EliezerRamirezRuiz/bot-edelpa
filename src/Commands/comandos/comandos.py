from Database import *
from discord.ext import commands


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
            result = await stock.get_data(str(message.content))

            await ctx.send(result) 
            
        except Exception as ex:
            await ctx.send(ex)


    @commands.command()
    async def estado_robot(self, ctx):
        """Function para obtener estado del robot\n
        Funcion por trabajar y arreglar"""

        await ctx.send("Consultando estado del robot")
        result = await robot.get_data()
        await ctx.send(result)

    
    @commands.command()
    async def ultimas_alertas(self, ctx):
        """Funcion que consulta la funcion `Alerta.ultimas_alertas_activas()` y obtiene el objeto Embed y
            lo retornamos. \n

        Funcion concluida y para utilizar"""
        
        await ctx.send("Obteniendo alertas")
        embed = await alerta.ultimas_alertas_activas()
        await ctx.send(embed=embed)