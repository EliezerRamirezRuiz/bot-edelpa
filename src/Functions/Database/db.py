import pyodbc 

server = 'EDELPA-PC061'
password = 'testuser1234'
database = 'Prueba'
username = 'testuser'

def con_sql():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+\
                                        server+';DATABASE='+database+\
                                            ';Trusted_Connection=yes;')
        print("Conexion realizada")
        return connection

    except Exception as error:
        print(f'error: {error}\ncause:{error.__context__}')


def get_data():
    with con_sql() as conn:
        cursor = conn.cursor()
        row = cursor.execute("SELECT @@version;")
        while row: 
            row = cursor.fetchone()
            print(row)


get_data()


