from Functions.Commands.Database.conexion_db import connection_sqlserver


async def obtener_stock(code:str, ctx):
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
        return f'obtener stock no puede:{ex}'

    finally:
        await cursor.close()
        await conn.close()


async def obtener_alerta(code:str, ctx):
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    try:
        conn = await connection_sqlserver()
        async with conn.cursor() as cursor:
            query = f" SELECT * FROM ALERTS WHERE AlertID = '{code}'" 
            print(query)
            await cursor.execute(query)
            row = await cursor.fetchone()
            return row

        
        
    except Exception as ex:
        return f'obtener alerta :{ex}'
        
    finally:
        await cursor.close()
        await conn.close()


async def estado_del_robot(ctx):
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    try:
        """codigo a ejecutar"""

        return 'Trabajando'
        
    except Exception as ex:
        return f'estado del robot :{ex}'
        
    finally:
        """finall operacion"""



async def reporte_dia(ctx):
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    try:
        """codigo a ejecutar"""

        return 'Trabajando'
        
    except Exception as ex:
        return f'estado del robot :{ex}'
        
    finally:
        """finall operacion"""