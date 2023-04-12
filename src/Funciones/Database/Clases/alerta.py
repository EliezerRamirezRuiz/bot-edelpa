
import aiohttp
import asyncio

from Funciones.Database.db import Database
from aiohttp.client_exceptions import ContentTypeError


class Alerta(Database):
    """Subclase heredada de Database, se encarga de las alertas 
    y contendra todos los metodos que tengan alguna relacion con
    las alertas"""

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
                query = f" EXEC LeerAlertas "

                await cursor.execute(query)
                row = await cursor.fetchall()

                print(row)
                return row

        except Exception as ex:
            print(f'obtener alerta :{ex}')

        finally:
            await cursor.close()
            await conn.close()


    async def alertas_automaticas(self):
        """Funcion para mandar mensaje automaticamente sin parar,
        se espera 5 segundos para volver a contactar la base de datos
        y traer aquellas alertas que esten activas"""

        while True:
            async with aiohttp.ClientSession() as session:

                await asyncio.sleep(3)
                lista_alertas = await self.get_data()

                if len(lista_alertas) == 0:
                    print('no hay alertas')

                else:
                    for data in lista_alertas:
                        mensaje = f'''situacion: {data[0]} ,problema: {data[1]} ,canal: {data[2]}'''
                        webhook_url = f'{self.base_url + data[3]}'

                        async with session.post(url=webhook_url,json={'content': mensaje}) as r:
                            try:
                                print(r.status)
                                print('listo')

                            except ContentTypeError as ex:
                                print(f'Error: Response {ex} is not in JSON format')


