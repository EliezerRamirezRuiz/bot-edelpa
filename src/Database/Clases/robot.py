from Database.database import Conexion
import discord

class Robot(Conexion):
    async def get_data(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una alerta """
        try:
            embed = discord.Embed(title='Trabajando')
            return embed

        except Exception as ex:
            embed = discord.Embed(title=f'{ex}')
            return embed

        finally:
            pass