from Database.db import Database
import discord

class Reporte(Database):
    async def get_data(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una alerta """
        try:
            embed = discord.Embed(title='Reporte',
                                  description='Ninguno')
            return embed

        except Exception as ex:
            embed = discord.Embed(title='Reporte',
                                  description=f'{ex}')
            return embed

        finally:
            """finall operacion"""
