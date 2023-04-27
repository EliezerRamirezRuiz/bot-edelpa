""" importaciones """
from aioodbc import Connection, connect
from datetime import datetime
from config.config import DSN
from discord import Embed


async def conexion_db() -> Connection:
    """Retornamos una conexion valida para conectarse a base de datos `SQL SERVER`"""
    try:
        connection = await connect(dsn=DSN['dsn'])
        return connection

    except Exception as ex:
        if isinstance(ex, TimeoutError):
            print('tiempo de ejecucion excedido')
        
        elif isinstance(ex, ):
            pass

# obtener la hora actual
def obtener_hora() -> datetime:
    return datetime.now()

# comprobamos si las horas son iguales
def comprobar_hora(hora_uno:datetime, hora_dos:datetime) -> bool:
    return hora_uno == hora_dos

# comprobar largo de lista si e mayor a 0
def comprobar_largo(lista:list) -> bool:
    return len(lista) > 0

# comprobar si cantidad es mayor
def comprobar_mayor(numero:int) -> bool:
    return numero > 0

# formatear la hora en hora y minutos
def formatear_hora(hora:datetime) -> str:
    return hora.strftime("%H:%M")


def create_embed(title=None, description=None, color=None, 
                    author:dict=None, footer=None, thumbnail=None, image=None, fields=None):
    """funcion para crear objetos embed de Discord, con los campos adicionales si es que existieran
    \n `Consideración`: Los atributos `atributo['nombre']` Si no son declarados arrojara un error llamada `Keyerror`,
    caso contrario pasa con `atributo.get('nombre')` lo dejara en none si no se encuentra."""
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
