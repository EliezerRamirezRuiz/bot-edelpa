"""Archivo que contiene el menu con multiples opciones 
que apretando alguna realiza la accion conrrespondiente"""
from discord import SelectOption, Interaction
from discord.ui import Select

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

# constante
VALUES = [
        SelectOption(label="Default", default=True, value="Default", description="default"),
        SelectOption(label="Consultar Stock", value="Consultar Stock", description="Consultar stock de producto X"),
        SelectOption(label="Estado Robot", value="Estado Robot", description="Saber el estado actual del robot - [Trabajando - Parado]"),
        SelectOption(label="Ultimas alertas activas", value="Ultimas alertas activas", description="Saber la informacion de las alertas desactivadas (TOP 10)"),
        SelectOption(label="Ultimas alertas desactivadas", value="Ultimas alertas desactivadas", description="Saber la informacion de las alertas desactivadas (TOP 10)"),
        SelectOption(label="Reporte del dia",  value="Reporte del dia", description="Saber la cantidad de alertas que se podrujeron por dia",),
    ]


class Menu(Select):
    def __init__(self, bot, ctx):
        self.bot = bot
        self.ctx = ctx
    
        super().__init__(custom_id="Menu", placeholder="Menu", min_values=1, 
                         max_values=1, options=VALUES, row=1)

    async def callback(self, interaccion:Interaction):
        opcion = self.values[0]
        match opcion:
            #caso 1
            case "Default":
                await interaccion.response.send_message('¡Opcion no valida! porfavor digite otra')

            # Caso 2
            case "Consultar Stock":
                try:                
                    await interaccion.response.send_message('Escriba el codigo a consultar:')
                    message = await self.bot.wait_for('message', check=lambda m: m.author == self.ctx.author, timeout=30.0)
                    embed = await stock.return_stock(str(message.content))
                    await interaccion.followup.send(embed=embed)

                except TimeoutError:
                    await self.ctx.send('Tiempo excedido')

            # Caso 3
            case "Estado Robot":
                await interaccion.response.send_message('Verificando')
                embed = await robot.obtener_datos()
                await self.ctx.send(embed=embed)

            # Caso 4
            case "Ultimas alertas activas":
                await interaccion.response.send_message("Obteniendo informacion...")
                embed = await alerta.retornar_alertas_activas(self.bot)
                await self.ctx.send(embed=embed)

            # Caso 5
            case "Ultimas alertas desactivadas":
                await interaccion.response.send_message("Obteniendo informacion...")
                embed = await alerta.retornar_alertas_desactivadas(self.bot)
                await self.ctx.send(embed=embed)

            #Caso 6
            case "Reporte del dia":
                await interaccion.response.send_message("Obteniendo reporte")
                embed = await reporte.get_data()
                await self.ctx.send(embed=embed)