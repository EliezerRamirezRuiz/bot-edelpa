"""Archivo que contiene el menu con multiples opciones 
que apretando alguna realiza la accion conrrespondiente"""
from discord import SelectOption, Interaction
from discord.ui import Select
from src.database import * 
from src.utils.funciones_utiles import tiempo_excedido


class OpcionesMenu:
    """ Clase simple que contiene los valores de las opciones a mostrar """
    values:list = [
            SelectOption(label="Default", default=True, value="Default"
                        , description="default"),

            SelectOption(label="Consultar Stock", value="Consultar Stock"
                        , description="Consultar stock de producto X"),
            
            SelectOption(label="Estado Robot", value="Estado Robot"
                        , description="Saber el estado actual del robot - [Trabajando - Parado]"),
            
            SelectOption(label="Ultimas alertas activas", value="Ultimas alertas activas"
                        , description="Saber la informacion de las alertas desactivadas (TOP 10)"),
            
            SelectOption(label="Ultimas alertas desactivadas", value="Ultimas alertas desactivadas"
                        , description="Saber la informacion de las alertas desactivadas (TOP 10)"),

            SelectOption(label="Reporte del dia",  value="Reporte del dia"
                        , description="Saber la cantidad de alertas que se podrujeron por dia",),
            ]


class Menu(Select):
    def __init__(self, bot, ctx):
        self.bot = bot
        self.ctx = ctx
    
        super().__init__(custom_id="Menu", placeholder="Menu", min_values=1, 
                         max_values=1, options=OpcionesMenu().values, row=1)

    async def callback(self, interaccion:Interaction):
        embed_tiempo_excedido = tiempo_excedido()
        opcion = self.values[0]
        match opcion:
            #caso 1
            case "Default":
                await interaccion.response.send_message(embed=embed_tiempo_excedido)

            # Caso 2
            case "Consultar Stock":
                try:                
                    await interaccion.response.send_message('Escriba el codigo a consultar:')
                    message = await self.bot.wait_for('message', check=lambda m: m.author == self.ctx.author, timeout=30.0)
                    embed = await instancia_stock.return_stock(str(message.content), self.ctx)
                    await self.ctx.send(embed=embed)

                except TimeoutError:
                    await self.ctx.send('Tiempo excedido')

            # Caso 3
            case "Estado Robot":
                await interaccion.response.send_message('Verificando')
                embed = await instancia_robot.get_data()
                await self.ctx.send(embed=embed)

            # Caso 4
            case "Estado Robot":
                await interaccion.response.send_message('Verificando')
                embed = await instancia_robot.get_data()
                await self.ctx.send(embed=embed)

            # Caso 5
            case "Ultimas alertas activas":
                await interaccion.response.send_message("Obteniendo informacion...")
                embed = await instancia_alerta.ultimas_alertas_activas(self.bot)
                await self.ctx.send(embed=embed)

            # Caso 6
            case "Ultimas alertas desactivadas":
                await interaccion.response.send_message("Obteniendo informacion...")
                embed = await instancia_alerta.ultimas_alertas_desactivadas(self.bot)
                await self.ctx.send(embed=embed)

            #Caso 7
            case "Reporte del dia":
                await interaccion.response.send_message("Obteniendo reporte")
                embed = await instancia_report.get_data()
                await self.ctx.send(embed=embed)