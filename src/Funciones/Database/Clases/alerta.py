"""Archivo """
import aiohttp
import asyncio
import discord
from Funciones.Database.db import Database
from aiohttp.client_exceptions import ContentTypeError


class Alerta(Database):
    """Subclase heredada de Database, se encarga de las alertas 
    y contendra todos los metodos que tengan alguna relacion con
    las alertas que sean llamados de comandos o menus con opciones
    programables"""

    def __init__(self) -> None:
        self.base_url = 'https://discordapp.com/api/webhooks/'
        super().__init__()


    async def get_data(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto muchas alertas, todo a traves de un 
        procedimiento almacenado """

        try:
            conn = await self.connection_sqlserver()
            async with conn.cursor() as cursor:
                query = f" EXEC ULTIMAS_ALERTAS "
                await cursor.execute(query)
                row = await cursor.fetchall()

                print(row)
                return row

        except Exception as ex:
            print(f'obtener alerta :{ex}')

        finally:
            await cursor.close()
            await conn.close()






