""" importaciones """
from aioodbc import Connection, connect
from datetime import datetime
from src.config.config import DSN
from discord import Embed
from pyodbc import ProgrammingError


async def conexion_db() -> Connection:
    """ Retornamos una conexion valida para conectarse a base de datos `SQL SERVER` """
    try:
        connection = await connect(dsn=DSN['dsn'])
        return connection

    except Exception as ex:
        if isinstance(ex, TimeoutError):
            print('tiempo de ejecucion excedido')
        
        elif isinstance(ex, ProgrammingError):
            print('Se intento cerrar una conexion')


def obtener_hora() -> datetime:
    """ Obtener la hora actual """
    return datetime.now()


def comprobar_hora(hora_uno:datetime, hora_dos:datetime) -> bool:
    """ Comprobamos si las horas son iguales """
    return hora_uno == hora_dos


def comprobar_largo(lista:list) -> bool:
    """ comprobar largo de lista si e mayor a 0 """
    return len(lista) > 0


def comprobar_mayor(numero:int) -> bool:
    """ Comprobar si cantidad es mayor """
    return numero > 0


def formatear_hora(hora:datetime) -> str:
    """ Formatear la hora en hora y minutos """
    return hora.strftime("%H:%M")


def formatear_fecha(date:datetime) -> str:
    return date.strftime(r'%Y-%m-%d')


def create_embed(title=None, description=None, color=None, 
                    author:dict=None, footer=None, thumbnail=None, image=None, fields=None):
    """Función para crear objetos embed de Discord, con los campos adicionales si es que existieran
    \n `Consideración`: Los atributos `atributo['nombre']` Si no son declarados arrojara un error llamada `Keyerror`,
    caso contrario pasa con `atributo.get('nombre')` lo dejara en None si no se encuentra."""
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


def tiempo_excedido():
    embed = create_embed(title='Tiempo excedido',
                description='ya no se puede responder la solicitud anterior')
    return embed