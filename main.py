# logging
import asyncio
import time

from src.app.bot import run_bot
from src.server.webserver import run_server
from src.logger.loggers import *

async def main() -> None:
    """Funcion que inicia el bot y carga las extensiones"""
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(run_bot())
            task2 = tg.create_task(run_server())

            print(f"started at {time.strftime('%X')}")

    except ExceptionGroup as ex:
        print(ex.with_traceback(), ex.__class__, ex.__context__)
    

if __name__ == '__main__':
    asyncio.run(main())