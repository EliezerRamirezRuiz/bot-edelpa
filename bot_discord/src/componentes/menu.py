# Discord clases
from discord.ext.commands import Bot
from discord import Interaction
from discord.ui import Select
# Clases
from src.database.alerta import AlertaBaseDeDatos
from src.database.stock import StockBaseDeDatos
from src.database.robot import RobotBaseDeDatos 
# Constantes
from src.config.config import VALUES
from logging import INFO, WARNING
# Funcion y variable
from logging import makeLogRecord
from src.logger.logger_app import my_handler


class Menu(Select):
    def __init__(self, bot:Bot, ctx):
        self.bot = bot
        self.ctx = ctx
        self.alerta = AlertaBaseDeDatos()
        self.stock = StockBaseDeDatos()
        self.robot = RobotBaseDeDatos()        
        super().__init__(custom_id="Menu", placeholder="Menu", min_values=1, max_values=1, options=VALUES, row=1)

    async def callback(self, interaccion:Interaction): 
        match self.values[0]:
            #caso 1
            case "Default":
                await interaccion.response.send_message('¡Opcion no valida! porfavor digite otra')

            # Caso 2
            case "Consultar Stock":
                try:
                    await interaccion.response.send_message('Escriba el codigo a consultar:')
                    message = await self.bot.wait_for('message', check=lambda m: m.author == self.ctx.author, timeout=30.0)
                    embed = await self.stock.return_stock(str(message.content)) 
                    await self.ctx.send(embed=embed)

                except Exception as ex:
                    my_handler.emit(makeLogRecord({
                        'msg': f"Ocurrio este error: {ex}", 
                        'levelno': WARNING, 
                        'levelname':'WARNING'}))            
                    if isinstance(ex, TimeoutError):
                        await self.ctx.send('Tiempo excedido')
                    else:
                        await self.ctx.send('Error, contactar con Areá TI')

            # Caso 3
            case "Estado Robot":
                try:                
                    embed = await self.robot.obtener_datos()
                    await interaccion.response.send_message(embed=embed)

                except Exception as ex:
                    my_handler.emit(makeLogRecord({
                        'msg': f"Ocurrio este error: {ex}", 
                        'levelno': WARNING, 
                        'levelname':'WARNING'}))                        
                    if isinstance(ex, TimeoutError):
                        await interaccion.followup.send('Tiempo excedido')

                    else:
                        await interaccion.followup.send('Error, consultar con el Areá TI')

            # Caso 4
            case "Ultimas alertas activas":
                try:                
                    embed = await self.alerta.retornar_alertas_activas(self.bot)
                    await interaccion.response.send_message(embed=embed)

                except Exception as ex:
                    my_handler.emit(makeLogRecord({
                        'msg': f"Ocurrio este error: {ex}", 
                        'levelno': WARNING, 
                        'levelname':'WARNING'}))                        
                    if isinstance(ex, TimeoutError):
                        await interaccion.followup.send('Tiempo excedido')
                    else:
                        await interaccion.followup.send('Error, consultar con el Areá TI')

            # Caso 5
            case "Ultimas alertas desactivadas":
                try:                
                    embed = await self.alerta.retornar_alertas_desactivadas(self.bot)
                    await interaccion.response.send_message(embed=embed)

                except Exception as ex:
                    my_handler.emit(makeLogRecord({
                        'msg': f"Ocurrio este error: {ex}", 
                        'levelno': WARNING, 
                        'levelname':'WARNING'}))    
                    if isinstance(ex, TimeoutError):
                        await interaccion.followup.send('Tiempo excedido')
                    else:

                        await interaccion.followup.send('Error, consultar con el Areá TI')