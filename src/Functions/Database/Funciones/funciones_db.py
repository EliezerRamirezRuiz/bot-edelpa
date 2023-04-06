import asyncio
import aiohttp

from Functions.Database.conexion_db import connection_sqlserver
from aiohttp.client_exceptions import ContentTypeError


base_url = 'https://discordapp.com/api/webhooks/'

links = {
    'General': '1088085873469423638/h89WN8y-vvQTTQhwu6Fszm6HuLhZ4QaVICxMyAfdudrizbV4QBCknwTYgv7H3U2VSGPa',
    'corte': '1093594193466757141/ORFvoLxFES6w0QoX_MC0A8XjoRcZegEQUOrexvhIjF7RAZBZrFqLUinHDRx_aplldqm-'}


async def obtener_stock(code:str):
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una Stock """
    try:
        conn = await connection_sqlserver()
        async with conn.cursor() as cursor:
            query = f" EXEC  ObtenerStock {code} " 
            await cursor.execute(query)
            row = await cursor.fetchone()

            if row is None:
                return 'codigo invalido'
            
            return row
        
    except Exception as ex:
        return f'obtener stock no puede:{ex.__class__.__context__}'

    finally:
        await cursor.close()
        await conn.close()


async def obtener_alertas():
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    try:
        conn = await connection_sqlserver()
        async with conn.cursor() as cursor:
            query = f" SELECT * FROM ALERTS WHERE AlertActivo = '1'" 
            print(query)
            await cursor.execute(query)
            row = await cursor.fetchall()
            return row


    except Exception as ex:
        return f'obtener alerta :{ex}'
        
    finally:
        await cursor.close()
        await conn.close()


async def estado_del_robot():
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    try:
        """codigo a ejecutar"""

        return 'Trabajando'
        
    except Exception as ex:
        return f'estado del robot :{ex}'
        
    finally:
        """finall operacion"""



async def reporte_dia():
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    try:
        """codigo a ejecutar"""

        return 'Trabajando'
        
    except Exception as ex:
        return f'estado del robot :{ex}'
        
    finally:
        """finall operacion"""


async def Leer_Alertas():
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una Stock """
    try:
        conn = await connection_sqlserver()
        async with conn.cursor() as cursor:
            query = f" EXEC  LeerAlertas " 
            await cursor.execute(query)
            row = await cursor.fetchall()

            if row is None:
                return 0
            
            return row
            
    except Exception as ex:
        print(ex)

    finally:
        await cursor.close()
        await conn.close()


async def return_data(list_link:dict=None):
    if list_link is None:
        list_link = []
        
    data = await Leer_Alertas()
    for i in data:
            key = i[1]
            value = i[2]
            list_link[key] = value
        
    print(list_link)




async def test():
    """Funcion para mandar mensaje automaticamente sin parar"""
    """while True:         
        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(30)
                webhook_url = f'{base_url + value}'
                async with session.post(url=webhook_url, json={'content': 'Buenas tardes'}) as r:
                    try:
                       print('listo')
                    except ContentTypeError:
                        print(f'Error: Response {i} is not in JSON format')
                        continue"""
    pass