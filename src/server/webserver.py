# import from
from quart import Quart
# import 
import asyncio
import aiohttp


app = Quart(__name__)


@app.route('/')
async def home():
    return "I'm alive"


async def run_server():
  await app.run_task()


async def peticion_server():
  while True:
    await asyncio.sleep(120)
    async with aiohttp.ClientSession() as session:
      async with session.get('http://127.0.0.1:5000') as response:
        print(f"""
        -------------------------------------------------------
        1)'Status:', {response.status}
        2)'Content-type:', {response.headers['content-type']}
        -------------------------------------------------------
        """)