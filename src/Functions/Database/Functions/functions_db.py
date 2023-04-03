from Functions.Database.db import connection_sqlserver


async def obtener_stock(code:str, ctx):
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una Stock """
    try:
        conn = await connection_sqlserver()
        async with conn.cursor() as cursor:

            query = f" SELECT * FROM MCHB WHERE MATNR = '{code}' " 
            print(query)
            
            await cursor.execute(query)
            row = await cursor.fetchone()

            if (len(row) > 0):
                return row
            else:
                return 'verifica el dato que estas ingresando e intenta de nuevo porfavor'
                
    except TimeoutError:
        return f'Error al conectarse a la base de datos,\
                    se Excedio del tiempo maximo'

    finally:
        await cursor.close()
        await conn.close()


async def obtener_alerta(ctx):
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    code = ''
    try:
        conn = await connection_sqlserver()
        async with conn.cursor() as cursor:
            query = f" SELECT * FROM ALERTS WHERE AlertID > {code} " 
            print(query)
            await cursor.execute(query)
            row = await cursor.fetchone()
            return row
        
    except TimeoutError:
        await ctx.send(f'Error al conectarse a la base de datos,\
                       se Excedio del tiempo maximo')
        
    finally:
        await cursor.close()
        await conn.close()


async def estado_del_robot(ctx):
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    try:
        """codigo a ejecutar"""

        return 'Trabajando'
        
    except TimeoutError:
        return f'Error al conectarse a la base de datos,\
                       se Excedio del tiempo maximo'
        
    finally:
        """finall operacion"""