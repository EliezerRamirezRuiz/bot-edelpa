import pyodbc 
import os

server = 'EDELPA-PC061'
password = 'testuser1234'
database = 'Prueba'
username = 'testuser'


async def con_sql():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+\
                                ';DATABASE='+database+';Trusted_Connection=yes;')
        return connection
        
    except Exception as error:
        print(f'error: {error}\ncause:{error.__context__}')