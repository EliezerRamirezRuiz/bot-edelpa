# Discord clases
from discord.ext.commands import Bot
from discord import Interaction
from discord.ui import Select
# Clases
from src.database.alerta import AlertaBaseDeDatos
from src.database.stock import StockBaseDeDatos
from src.database.robot import RobotBaseDeDatos 
from src.database.reporte import ReporteBaseDeDatos
# Funciones
from src.config.config import VALUES


# Variables
alerta = AlertaBaseDeDatos()
reporte = ReporteBaseDeDatos()
stock = StockBaseDeDatos()
robot = RobotBaseDeDatos()

class Menu(Select):
    def __init__(self, bot:Bot):
        self.bot = bot
        super().__init__(custom_id="Menu", placeholder="Menu", min_values=1, max_values=1, options=VALUES, row=1)

    async def callback(self, interaccion:Interaction):
        ctx = await self.bot.get_context(interaccion) 
        OPCION = self.values[0]
    
        match OPCION:
            #caso 1
            case "Default":
                await interaccion.response.send_message('¡Opcion no valida! porfavor digite otra')

            # Caso 2
            case "Consultar Stock":
                try:                
                    await interaccion.response.send_message('Escriba el codigo a consultar:')
                    message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
                    embed = await stock.return_stock(str(message.content))
                    await interaccion.followup.send(embed=embed)

                except TimeoutError:
                    await interaccion.followup.send('Tiempo excedido')

            # Caso 3
            case "Estado Robot":
                try:                
                    embed = await robot.obtener_datos()
                    await interaccion.response.send_message(embed=embed)

                except TimeoutError:
                    await interaccion.followup.send('Tiempo excedido')


            # Caso 4
            case "Ultimas alertas activas":
                try:                
                    embed = await alerta.retornar_alertas_activas(self.bot)
                    await interaccion.response.send_message(embed=embed)

                except TimeoutError:
                    await interaccion.followup.send('Tiempo excedido')


            # Caso 5
            case "Ultimas alertas desactivadas":
                try:                
                    embed = await alerta.retornar_alertas_desactivadas(self.bot)
                    await interaccion.response.send_message(embed=embed)

                except TimeoutError:
                    await interaccion.followup.send('Tiempo excedido')


            #Caso 6
            case "Reporte del dia":
                try:                
                    embed = await reporte.get_data()
                    await interaccion.response.send_message(embed=embed)

                except TimeoutError:
                    await interaccion.followup.send('Tiempo excedido')