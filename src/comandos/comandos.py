from discord.ext.commands import Cog, Bot 
from discord.ext.commands import command 
# Clases
from src.database.alerta import AlertaBaseDeDatos
from src.database.stock import StockBaseDeDatos
from src.database.robot import RobotBaseDeDatos 
from src.database.reporte import ReporteBaseDeDatos

# Variables
alerta = AlertaBaseDeDatos()
reporte = ReporteBaseDeDatos()
stock = StockBaseDeDatos()
robot = RobotBaseDeDatos()


class ComandosPrincipales(Cog):
    """instancia del bot para controlar los comandos de manera escalable"""
    def __init__(self, bot):
        self.bot = bot


    @command()
    async def consultar_stock(self, ctx, codigo):
        """Funcion que consultar stock a pedir, manda mensaje para que el usuario sepa 
        que debe mandar una respuesta para consultar el stock"""
        try:
            embed = await stock.return_stock(codigo)
            await ctx.send(embed=embed)

        except Exception as ex:
                await ctx.send(f'''Error desconocido, porfavor contactar con el encargado de informatica, {ex}''')
                


    @command()
    async def estado_robot(self, ctx):
        """Function para obtener estado del robot\n
        Funcion por trabajar y arreglar"""

        await ctx.send("Consultando estado del robot")
        embed =  await robot.obtener_datos()
        await ctx.send(embed=embed)

    
    @command()
    async def alertas_activas(self, ctx):
        """Funcion que consulta la funcion `Alerta.ultimas_alertas_activas()` 
        y obtiene el objeto Embed y lo retornamos. \n
        Funcion concluida y para utilizar"""

        await ctx.send("Obteniendo alertas")
        embed = await alerta.retornar_alertas_activas(self.bot)
        await ctx.send(embed=embed)


    @command()
    async def alertas_desactivadas(self, ctx):
        """Funcion que consulta la funcion `Alerta.ultimas_alertas_desactivadas()` y obtiene el objeto Embed y
            lo retornamos. \n
        Funcion concluida y para utilizar"""
        
        await ctx.send("Obteniendo ultimas alertas desactivadas")
        embed = await alerta.retornar_alertas_desactivadas(self.bot)
        await ctx.send(embed=embed)


    @Cog.listener()
    async def on_ready(self):
        print('Comandos.py en linea.')


async def setup(bot:Bot): 
    print('He sido cargado comandos.py')
    await bot.add_cog(ComandosPrincipales(bot))


async def teardown(bot:Bot):
    print('He sido bajado comandos.py!')
    await bot.remove_cog(ComandosPrincipales(bot))