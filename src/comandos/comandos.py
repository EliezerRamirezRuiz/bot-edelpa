from discord.ext import commands
from src.database import *

class ComandosPrincipales(commands.Cog):
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
            embed = await instancia_stock.return_stock(str(message.content))
            await ctx.send(embed=embed)

        except Exception as ex:
            if isinstance(ex, ValueError):
                await ctx.send('Valor invalido')

            if isinstance(ex, TimeoutError):
                await ctx.send('Se ha excedido el tiempo de respuesta')

            else:
                await ctx.send('Error desconocido, porfavor contactar con el encargado de informatica')


    @commands.command()
    async def estado_robot(self, ctx):
        """Function para obtener estado del robot\n
        Funcion por trabajar y arreglar"""

        await ctx.send("Consultando estado del robot")
        embed =  await instancia_robot.get_data()
        await ctx.send(embed=embed)

    
    @commands.command()
    async def alertas_activas(self, ctx):
        """Funcion que consulta la funcion `Alerta.ultimas_alertas_activas()` 
        y obtiene el objeto Embed y lo retornamos. \n

        Funcion concluida y para utilizar"""
        
        await ctx.send("Obteniendo alertas")
        embed = await instancia_alerta.ultimas_alertas_activas(self.bot)
        await ctx.send(embed=embed)


    @commands.command()
    async def alertas_desactivadas(self, ctx):
        """Funcion que consulta la funcion `Alerta.ultimas_alertas_desactivadas()` y obtiene el objeto Embed y
            lo retornamos. \n
        Funcion concluida y para utilizar"""
        
        await ctx.send("Obteniendo ultimas alertas desactivadas")
        embed = await instancia_alerta.ultimas_alertas_desactivadas(self.bot)
        await ctx.send(embed=embed)