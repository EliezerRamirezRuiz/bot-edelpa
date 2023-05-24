from discord.ext.commands import Cog, Bot 
from discord.ext.commands import command 
# Logger
from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO, WARNING
# Clases
from src.database.alerta import AlertaBaseDeDatos
from src.database.stock import StockBaseDeDatos
from src.database.robot import RobotBaseDeDatos 


class ComandosPrincipales(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.alerta = AlertaBaseDeDatos()
        self.stock = StockBaseDeDatos()
        self.robot = RobotBaseDeDatos()


    @command()
    async def consultar_stock(self, ctx, codigo:str):
        try:
            embed = await self.stock.return_stock(codigo)
            await ctx.send(embed=embed)

        except Exception as ex:
            my_handler.emit(makeLogRecord({
                'msg': f"Comandos.py en linea.", 
                'levelno': WARNING, 
                'levelname':'WARNING'}))


    @command()
    async def estado_robot(self, ctx):
        try:
            embed =  await self.robot.obtener_datos()
            await ctx.send(embed=embed)
        
        except Exception as ex:
            my_handler.emit(makeLogRecord({
                'msg': f"Comandos.py en linea.", 
                'levelno': WARNING, 
                'levelname':'WARNING'}))
    

    @command()
    async def alertas_activas(self, ctx):
        try:
            embed = await self.alerta.retornar_alertas_activas(self.bot)
            await ctx.send(embed=embed)
        
        except Exception as ex:
            my_handler.emit(makeLogRecord({
                'msg': f"Comandos.py en linea.", 
                'levelno': WARNING, 
                'levelname':'WARNING'}))


    @command()
    async def alertas_desactivadas(self, ctx):
        try:
            embed = await self.alerta.retornar_alertas_desactivadas(self.bot)
            await ctx.send(embed=embed)

        except Exception as ex:
            my_handler.emit(makeLogRecord({
                'msg': f"Comandos.py en linea.", 
                'levelno': INFO, 
                'levelname':'INFO'}))


    @Cog.listener()
    async def on_ready(self):
        my_handler.emit(makeLogRecord({
            'msg': f"Comandos.py en linea.", 
            'levelno': INFO, 
            'levelname':'INFO'}))


async def setup(bot:Bot): 
    await bot.add_cog(ComandosPrincipales(bot))
    my_handler.emit(makeLogRecord({
        'msg': f"He sido cargado comandos.py", 
        'levelno': INFO, 
        'levelname':'INFO'}))


async def teardown(bot:Bot):
    await bot.remove_cog(ComandosPrincipales(bot))
    my_handler.emit(makeLogRecord({
        'msg': f"He sido bajado comandos.py!", 
        'levelno': INFO, 
        'levelname':'INFO'}))