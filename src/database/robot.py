from src.utils.funciones_utiles import create_embed

from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO, WARNING

class RobotBaseDeDatos():
    async def obtener_datos(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una alerta """
        try:
            embed = create_embed(title='Trabajando')

        except Exception as ex:
            my_handler.emit(makeLogRecord({'msg': f"error: {ex}", 'levelno': INFO, 'levelname':'INFO'}))

        finally:
            return embed