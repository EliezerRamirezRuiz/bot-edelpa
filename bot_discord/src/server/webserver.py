from src.logger.logger_app import my_handler
from quart.logging import _setup_logging_queue

from logging import makeLogRecord, getLogger
from logging import INFO, WARNING
from quart import Quart

import asyncio
import aiohttp


app = Quart(__name__)


_setup_logging_queue(my_handler)
getLogger('quart.app').addHandler(my_handler)
getLogger('quart.serving').addHandler(my_handler)


@app.route('/')
async def home():
    return "I'm alive"


async def run_server():
  await app.run_task(port=5500, debug=True)


async def peticion_server():
  while True:
    try:
      await asyncio.sleep(120)
      async with aiohttp.ClientSession('http://127.0.0.1:5500') as session:
        async with session.get('/') as response:
          my_handler.emit(makeLogRecord({
            'msg': f"Status: {response.status}", 
            'levelno': INFO,
            'levelname':'INFO'}))
          
    except Exception as ex:
      my_handler.emit(makeLogRecord({
        'msg': f"Ocurrio este error: {ex}", 
        'levelno': WARNING, 
        'levelname':'WARNING'}))         