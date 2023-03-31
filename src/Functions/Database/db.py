import aioodbc


server = 'EDELPA-PC061'
password = 'testuser1234'
database = 'BDsap'
username = 'testuser'


async def connection_sqlserver():
    try:
        dsn = 'DRIVER={SQL Server};SERVER=' + server+';DATABASE='+database + ';Trusted_Connection=yes;'
        connection = await aioodbc.connect(dsn=dsn)
        return connection

    except TimeoutError as error:
        print(f'error: {error}\ncause:{error.__context__}')


async def get_stock(code:str, ctx):
    """ Funcion para traer datos de la base de datos SQL Server, 
    para ser mas exacto una alerta """
    try:
        conn = await connection_sqlserver()
        async with conn.cursor() as cursor:
            query = f"SELECT * FROM MCHB WHERE MATNR = '{code}'" 
            print(query)
            await cursor.execute(query)
            row = await cursor.fetchone()
            return row
                
    except TimeoutError as error:
        await ctx.send(f'Error al conectarse a la base de datos\
                       Error:{error}')

    finally:
        await cursor.close()
        await conn.close()


async def get_alert(ctx):
    """Function to get data from database SQL Server, 
    to be exactly one stock"""
    try:
        pass
    except:
        pass
    finally:
        pass

