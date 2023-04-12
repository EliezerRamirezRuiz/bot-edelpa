from Funciones.Database.db import Database


class Robot(Database):
    async def get_data(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una alerta """
        try:
            """codigo a ejecutar"""

            return 'Trabajando'

        except Exception as ex:
            return f'estado del robot :{ex}'

        finally:
            """finall operacion"""