#import
import aioodbc
#import through from 
from datetime import datetime
from aioodbc.connection import _ContextManager
from src.config.config import (DRIVER,SERVER,DATABASE)
from discord import Embed


async def conexion_db() -> _ContextManager:
    DSN = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
    try:
        connection = await aioodbc.connect(DSN)
        return connection

    except Exception as ex:
        raise ex


def obtener_hora() -> datetime:
    return datetime.now()


async def comprobar_hora(hora:datetime) -> bool:
    now = await hora
    return now == obtener_hora()


def comprobar_largo(lista:list) -> bool:
    return len(lista) > 0


def comprobar_mayor(numero:int) -> bool:
    return numero > 0


def create_embed(title=None, description=None, color=None, author:list=None, footer=None, thumbnail=None, image=None, fields=None):
    embed = Embed(title=title, description=description, color=color)

    if author:
        embed.set_author(name=author['name'], url=author.get('url'), icon_url=author.get('icon_url'))

    if footer:
        embed.set_footer(text=footer['text'], icon_url=footer.get('icon_url'))

    if thumbnail:
        embed.set_thumbnail(url=thumbnail)

    if image:
        embed.set_image(url=image)

    if fields:
        for field in fields:
            embed.add_field(name=field['name'], value=field['value'], inline=field.get('inline', True))

    return embed
