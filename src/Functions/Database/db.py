import pyodbc 
import os
import pyodbc

try:
    password = os.getenv('PASSWORD')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Prueba;UID=me;PWD=%s'.format(password))

except Exception as error:
    print(f'error: {error.__cause__}')