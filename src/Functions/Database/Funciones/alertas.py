from Functions.Database.conexion_db import Database
from aiohttp.client_exceptions import ContentTypeError

import aiohttp
import asyncio


class LeerAlerta(Database):
    def __init__(self) -> None:
        self.base_url = 'https://discordapp.com/api/webhooks/'
        super().__init__()


    async def query(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto muchas alertas """
        try:
            conn = await self.connection_sqlserver()
            async with conn.cursor() as cursor:
                query = f" EXEC LeerAlertas "

                await cursor.execute(query)
                row = await cursor.fetchall()

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

                await asyncio.sleep(5)
                lista_alertas = await self.query()

                if len(lista_alertas) == 0:
                    continue

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


