""" Importaciones """
from discord import Embed
from src.database.db import conexion_db
from src.utils.funciones_utiles import (comprobar_hora, comprobar_largo, 
                            comprobar_mayor, obtener_hora, formatear_hora, 
                            formatear_fecha, create_embed)

class AlertaDB():
    """
    Clase se encarga de las alertas y contendra todos los metodos que tengan alguna relacion con
    las alertas que sean llamados de comandos o menus con opciones
    """

    async def alertas_activas(self) -> list:
        """ Funcion que trae las ultimas alertas activas """
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC ULTIMAS_ALERTAS_ACTIVAS "
                    await cursor.execute(query)
                    row = await cursor.fetchall()
                    if row is None:
                        return []
                
                    return row 

        except Exception as ex:
            if isinstance(ex, TimeoutError):
                print('Tiempo excedido')
            
            else:
                print('Error desconocido')


    async def alertas_desactivadas(self):
        """ Funcion que trae las ultimas alertas inactivas """
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC ULTIMAS_ALERTAS_DESACTIVADAS "
                    await cursor.execute(query)
                    row = await cursor.fetchall()
                    if row is None:
                        return []
                
                    return row 
                
        except Exception as ex:
            if isinstance(ex, TimeoutError):
                print('Tiempo excedido')
            
            else:
                print('Error desconocido')


    async def retornar_alertas_activas(self, bot, lista=None) -> Embed:
        """Funcion que trae los datos de la funcion `alertas_activas()` se manipulan para presentar
        y entregar de una manera mas ordenada. En caso que no contenga alertas activas se mandara 
        un mensaje que le informe al usuario que no hay alertas"""
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
        """Funcion que trae los datos de la funcion `alertas_desactivadas()`
        se manipulan para presentar y entregar de una manera mas 
        ordenada. """

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