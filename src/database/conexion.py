from aioodbc import Connection, connect
from src.config.config import DSN

from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO, WARNING


async def conexion_db() -> Connection:
    """ Retornamos una conexion valida para conectarse a base de datos `SQL SERVER` """
    try:
        connection = await connect(dsn=DSN)
        return connection

    except Exception as ex:
            my_handler.emit(makeLogRecord({'msg': f"error: {ex}", 'levelno': INFO, 'levelname':'INFO'}))


