from discord import Embed
from src.database.conexion import conexion_db
from src.utils.funciones_utiles import (comprobar_largo, formatear_hora, formatear_fecha, create_embed)

from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO, WARNING


class AlertaBaseDeDatos():
    async def alertas_activas(self) -> list:
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC ULTIMAS_ALERTAS_ACTIVAS "
                    await cursor.execute(query)
                    row = await cursor.fetchall()

                    if row is not None:
                        return row
                    else:
                        return [] 

        except Exception as ex:
            my_handler.emit(makeLogRecord({'msg': f"error: {ex}", 'levelno': INFO, 'levelname':'INFO'}))


    async def alertas_desactivadas(self):
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC ULTIMAS_ALERTAS_DESACTIVADAS "
                    await cursor.execute(query)
                    row = await cursor.fetchall()

                    if row is not None:
                        return row
                    else:
                        return [] 
                
        except Exception as ex:
            my_handler.emit(makeLogRecord({'msg': f"error: {ex}", 'levelno': INFO, 'levelname':'INFO'}))

                
    async def retornar_alertas_activas(self, bot, lista=None) -> Embed:
        datos = await self.alertas_activas()

        if lista is None:
            lista = []

        if comprobar_largo(datos) is True:
            for i in datos:
                lista.append({'name':f'Problema alerta: {i[0]}', 
                                "value":f'''Error: {i[1]}
                                 Estado: {i[2]}
                                 Fecha: {formatear_fecha(i[3])}
                                 Hora: {formatear_hora(i[3])}''', 'inline':False,})
            
            embed = create_embed(
                title='Ultimas alertas activas', description='Lista de alertas activas', color=0x00ff00, 
                author={'name':f'{bot.user.name}','url':'https://www.edelpa.cl/','icon_url':f'{bot.user.avatar.url}'},
                footer={'text':'Envases del Pacifico - Edelpa'}, 
                fields=lista)
            
            return embed
        
        else:
            embed = create_embed(
                title='Ultimas alertas activas', description='Lista de alertas activas', color=0x00ff00, 
                author={'name':f'{bot.user.name}','url':'https://www.edelpa.cl/','icon_url':f'{bot.user.avatar.url}'},
                footer={'text':'Envases del Pacifico - Edelpa'}, 
                fields=[{'name':'No hay alertas activas', "value":'Información no disponible', 'inline':False,}])
            
            return embed


    async def retornar_alertas_desactivadas(self, bot, lista=None) -> Embed:
        datos = await self.alertas_desactivadas()

        if lista is None:
            lista = []

        if comprobar_largo(datos) is True:
            for i in datos:
                lista.append({'name':f'Problema alerta: {i[0]}', 
                                "value":f'''Error: {i[1]}
                                 Estado: {i[2]}
                                 Fecha: {formatear_fecha(i[3])}
                                 Hora: {formatear_hora(i[3])}''', 'inline':False,})
            
            embed = create_embed(
                title='Ultimas alertas desactivadas', description='Lista de alertas desactivadas', color=0x00ff00, 
                author={'name':f'{bot.user.name}','url':'https://www.edelpa.cl/','icon_url':f'{bot.user.avatar.url}'},
                footer={'text':'Envases del Pacifico - Edelpa'}, 
                fields=lista)
            
            return embed
        
        else:
            embed = create_embed(
                title='Ultimas alertas desactivadas', description='Lista de alertas activas', color=0x00ff00, 
                author={'name':f'{bot.user.name}','url':'https://www.edelpa.cl/','icon_url':f'{bot.user.avatar.url}'},
                footer={'text':'Envases del Pacifico - Edelpa'}, 
                fields=[{'name':'No hay alertas activas', "value":'Información no disponible', 'inline':False,}])
            
            return embed