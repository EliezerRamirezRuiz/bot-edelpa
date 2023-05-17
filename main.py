# logging
import asyncio
import time

from src.app.bot import run_bot
from src.server.webserver import run_server


async def main() -> None:
    """Funcion que inicia el bot y carga las extensiones"""
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(run_bot())
            task2 = tg.create_task(run_server())

            print(f"started at {time.strftime('%X')}")
 
    except Exception as ex:
        if isinstance(ex, KeyboardInterrupt):
            print('finalizo el ciclo')
        else:
            print(f'paso esto: {ex}')
    

if __name__ == '__main__':
    asyncio.run(main())