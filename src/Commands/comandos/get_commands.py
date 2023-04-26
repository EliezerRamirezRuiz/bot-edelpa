from Database.Clases import *
from discord.ext import commands


class GetCommands(commands.Cog):
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
            embed = await stock.return_stock(str(message.content))
            await ctx.send(embed=embed)


        except Exception as ex:
            await ctx.send(ex)


    @commands.command()
    async def estado_robot(self, ctx):
        """Function para obtener estado del robot\n
        Funcion por trabajar y arreglar"""

        await ctx.send("Consultando estado del robot")
        embed = await robot.get_data()
        await ctx.send(embed=embed)

    
    @commands.command()
    async def alertas_activas(self, ctx):
        """Funcion que consulta la funcion `Alerta.ultimas_alertas_activas()` 
        y obtiene el objeto Embed y lo retornamos. \n

        Funcion concluida y para utilizar"""
        
        await ctx.send("Obteniendo alertas")
        embed = await alerta.ultimas_alertas_activas()
        await ctx.send(embed=embed)


    @commands.command()
    async def alertas_desactivadas(self, ctx):
        """Funcion que consulta la funcion `Alerta.ultimas_alertas_desactivadas()` y obtiene el objeto Embed y
            lo retornamos. \n

        Funcion concluida y para utilizar"""
        
        await ctx.send("Obteniendo ultimas alertas desactivadas")
        embed = await alerta.ultimas_alertas_desactivadas()
        await ctx.send(embed=embed)