# asyncio
from asyncio import TaskGroup, run
from logging import makeLogRecord
from logging import INFO, WARNING
# aplicacion
from src.app.bot import run_bot
from src.server.webserver import run_server
from src.logger.logger_app import my_handler
# tiempo 
import time


async def main() -> None:
    """Funcion que inicia el bot y carga las extensiones"""
    try:
        async with TaskGroup() as tg:
            task1 = tg.create_task(run_bot())
            task2 = tg.create_task(run_server())
            my_handler.emit(makeLogRecord(
                {'msg': f"started at {time.strftime('%X')}", 'levelno': INFO, 'levelname':'INFO'}))

    except ExceptionGroup as ex:
        my_handler.emit(makeLogRecord(
            {'msg': f'''Ocurrio el siguiente error: {ex.with_traceback()}, {ex.__class__}, {ex.__context__}''',
              'levelno': WARNING, 'levelname':'WARNING'}))        
    

if __name__ == '__main__':
    run(main())