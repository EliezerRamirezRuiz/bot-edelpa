import asyncio
import aiohttp
from aiohttp.client_exceptions import ContentTypeError

base_url = 'https://discordapp.com/api/webhooks/'


complement = {
    'General': '1088085873469423638/h89WN8y-vvQTTQhwu6Fszm6HuLhZ4QaVICxMyAfdudrizbV4QBCknwTYgv7H3U2VSGPa'}


async def test():
    """Funcion para mandar mensaje automaticamente sin parar"""
    async with aiohttp.ClientSession() as session:
        await asyncio.sleep(5)
        for i, (key, value) in enumerate(complement.items()):
            webhook_url = f'{base_url + value}'
            async with session.post(url=webhook_url, json={'content': 'Buenas tardes'}) as r:
                try:
                    print('listo')
                except ContentTypeError:
                    print(f'Error: Response {i} is not in JSON format')
                    continue
