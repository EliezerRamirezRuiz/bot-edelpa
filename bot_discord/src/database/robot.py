from src.utils.funciones_utiles import create_embed
from src.logger.logger_app import my_handler

from logging import makeLogRecord
from logging import INFO


class RobotBaseDeDatos():
    async def obtener_datos(self):
        try:
            embed = create_embed(title='Trabajando')
            return embed
        
        except Exception as ex:
            my_handler.emit(makeLogRecord({'msg': f"error: {ex}", 'levelno': INFO, 'levelname':'INFO'}))


