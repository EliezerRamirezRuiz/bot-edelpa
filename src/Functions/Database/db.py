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

    except Exception:
        return f'No fue posible conectarse a la base de datos SQL Server,\
                    porfavor verifique credenciales y configuracion'



