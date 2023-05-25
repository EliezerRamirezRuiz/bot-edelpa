from discord import app_commands, Interaction 
from discord.ext.commands import Bot, Cog
from discord.ui import View

from src.database.alerta import AlertaBaseDeDatos
from src.database.stock import StockBaseDeDatos
from src.database.robot import RobotBaseDeDatos 
from src.componentes.menu import Menu
from src.logger.logger_app import my_handler

from logging import makeLogRecord
from logging import INFO, WARNING


class SlashComandos(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.stock = StockBaseDeDatos()
        self.robot = RobotBaseDeDatos()
        self.alerta = AlertaBaseDeDatos()


    @app_commands.command(name='menu', description='Ejecuta el comando !menu')
    async def menu(self, interaccion: Interaction) -> None:
        try:
            await interaccion.response.defer()            
            ctx = await self.bot.get_context(interaccion)
            select = Menu(self.bot, ctx)
            view = View(timeout=180)
            view.add_item(select)
            await interaccion.followup.send(view=view)

        
        except Exception as ex:
            my_handler.emit(makeLogRecord({
                'msg': f"Ocurrio este error: {ex}", 
                'levelno': WARNING, 
                'levelname':'WARNING'}))
            await interaccion.followup.send('Error, consultar con el Areá TI')


    @app_commands.describe(codigo="""Código requerido para buscar el stock, Ejemplo: 'EP100000000006000621850000500010'  """)
    @app_commands.command(name='consultar_stock', description='Trae los datos del stock a consultar')
    async def consultar_stock(self, interaccion: Interaction, codigo:str) -> None:
        try:
            await interaccion.response.defer()
            embed = await self.stock.return_stock(str(codigo))     
            await interaccion.followup.send(embed=embed)

        except Exception as ex:        
            my_handler.emit(makeLogRecord({
                'msg': f"Ocurrio este error: {ex}", 
                'levelno': WARNING, 
                'levelname':'WARNING'}))
            await interaccion.followup.send('Error, consultar con el Areá TI')     


    @app_commands.command(name='ultimas_alertas_activas', description='Trae las ultimas alertas desactivadas')
    async def alertas_activas(self, interaccion: Interaction) -> None:
        try:
            await interaccion.response.defer()            
            embed = await self.alerta.retornar_alertas_activas(self.bot)
            await interaccion.followup.send(embed=embed)
        
        except Exception as ex:       
            my_handler.emit(makeLogRecord({
                'msg': f"Ocurrio este error: {ex}", 
                'levelno': WARNING, 
                'levelname':'WARNING'}))
            await interaccion.followup.send('Error, consultar con el Areá TI')     


    @app_commands.command(name='ultimas_alertas_desactivadas', description='Trae las ultimas alertas desactivadas')
    async def alertas_desactivadas(self, interaccion: Interaction) -> None:
        try:
            await interaccion.response.defer()
            embed = await self.alerta.retornar_alertas_desactivadas(self.bot)
            await interaccion.followup.send(embed=embed)

        except Exception as ex:
            my_handler.emit(makeLogRecord({
                'msg': f"Ocurrio este error: {ex}",
                'levelno': WARNING,
                'levelname':'WARNING'}))
            await interaccion.followup.send('Error, consultar con el Areá TI')

    @app_commands.command(name='estado_robot', description='Trae el estado de robot')
    async def estado_robot(self, interaccion: Interaction) -> None:
        try:
            await interaccion.response.defer()
            embed =  await self.robot.obtener_datos()
            await interaccion.response.send_message(embed=embed)

        except Exception as ex:
            my_handler.emit(makeLogRecord({
                'msg': f"Ocurrio este error: {ex}",
                'levelno': WARNING,
                'levelname':'WARNING'}))
            await interaccion.followup.send('Error, consultar con el Areá TI')


    @Cog.listener()
    async def on_ready(self):
        my_handler.emit(makeLogRecord({
            'msg': f"slash.py online.",
            'levelno': INFO,
            'levelname':'INFO'}))


async def setup(bot:Bot):
    await bot.add_cog(SlashComandos(bot))
    my_handler.emit(makeLogRecord({
        'msg': f"he sido cargado slash.py",
        'levelno': INFO, 
        'levelname':'INFO'}))


async def teardown(bot:Bot):
    await bot.remove_cog(SlashComandos(bot))
    my_handler.emit(makeLogRecord({
        'msg': f"He sido descargado slash.py!",
        'levelno': INFO, 
        'levelname':'INFO'}))