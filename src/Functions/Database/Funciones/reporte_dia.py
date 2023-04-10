from Functions.Database.conexion_db import Database


class ReporteDia(Database):
    async def query(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una alerta """
        try:
            """codigo a ejecutar"""

            return 'Trabajando'

        except Exception as ex:
            return f'estado del robot :{ex}'

        finally:
            """finall operacion"""
