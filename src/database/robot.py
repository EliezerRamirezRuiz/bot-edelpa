from src.database.procedimientos import ProcedimientosAlmacenados
import discord

class RobotBaseDeDatos():
    def __init__(self) -> None:
        self.procedimiento = ProcedimientosAlmacenados()


    async def obtener_datos(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una alerta """
        try:
            embed = discord.Embed(title='Trabajando')

        except Exception as ex:
            embed = discord.Embed(title=f'{ex}')

        finally:
            return embed