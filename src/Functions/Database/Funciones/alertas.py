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
                query = f" SELECT * FROM ALERTS WHERE AlertActivo = '1'"
                print(query)
                await cursor.execute(query)
                row = await cursor.fetchall()
                print(row)

                return row

        except Exception as ex:
            print(f'obtener alerta :{ex}')

        finally:
            await cursor.close()
            await conn.close()


    async def return_data(self, list_link: dict = None):
        """ Funcion para obtener los datos y estructurarlos en un diccionario 
        para posteriormente ser manipulados """
        try:
            data = await self.query()

            if list_link is None:
                list_link = {}

            if data == None:
                pass

            else:
                for t in data:
                    key = t[2]
                    value = t[3]
                    list_link[key] = value

                return list_link

        except Exception as ex:
            print(ex)


    async def test(self):
        """Funcion para mandar mensaje automaticamente sin parar"""
        while True:
            async with aiohttp.ClientSession() as session:
                await asyncio.sleep(5)
                values = await self.return_data()
                for i, value in enumerate(values.values()):
                    print(i, value)
                    webhook_url = f'{self.base_url + value}'
                    async with session.post(url=webhook_url,
                                        json={'content': 'Buenas tardes'}) as r:
                        try:
                            print('listo')

                        except ContentTypeError as ex:
                            print(f'Error: Response {ex} is not in JSON format')