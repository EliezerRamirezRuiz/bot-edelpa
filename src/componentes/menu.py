"""Archivo que contiene el menu con multiples opciones 
que apretando alguna realiza la accion conrrespondiente"""
from discord import (SelectOption, Interaction)
from discord.ui import Select
from src.database import * 


class Opciones:
    """ Clase simple que contiene los valores de las opciones a mostrar """
    values:list = [
            SelectOption(label="Default", default=True, value="Default"
                        , description="default"),

            SelectOption(label="Consultar Stock", value="Consultar Stock"
                        , description="Consultar stock de producto X"),
            
            SelectOption(label="Estado Robot", value="Estado Robot"
                        , description="Saber el estado actual del robot"),
            
            SelectOption(label="Ultimas alertas activas", value="Ultimas alertas activas"
                        , description="Saber la cantidad de Bobinas que contiene un pallet"),
            
            SelectOption(label="Reporte del dia",  value="Reporte del dia"
                        , description="Saber la cantidad de alertas que se podrujeron por dia",),
            ]


class Menu(Select):
    def __init__(self, bot, ctx, bot_command):
        self.bot = bot
        self.ctx = ctx
        self.bot_command = bot_command

        super().__init__(custom_id="Menu", placeholder="Menu", min_values=1, 
                         max_values=1, options=Opciones().values, row=2)

    async def callback(self, interaccion:Interaction):
        opcion = self.values[0]
        match opcion:
            # Caso 1
            case "Consultar Stock":
                await interaccion.response.send_message('Escriba el codigo a consultar:')
                message = await self.bot.wait_for('message', check=lambda m: m.author == self.ctx.author, timeout=30.0)
                embed = await instancia_stock .return_stock(str(message.content), self.ctx)
                await self.ctx.send(embed=embed)


            # Caso 2
            case "Estado Robot":
                await interaccion.response.send_message('Verificando')
                embed = await instancia_robot.get_data()
                await self.ctx.send(embed=embed)


            # Caso 3
            case "Ultimas alertas activas":
                await interaccion.response.send_message("Obteniendo alertas...")
                embed = await instancia_alerta.ultimas_alertas_activas()
                await self.ctx.send(embed=embed)


            #Caso 4
            case "Reporte del dia":
                await interaccion.response.send_message("Obteniendo reporte")
                embed = await instancia_report.get_data()
                await self.ctx.send(embed=embed)


