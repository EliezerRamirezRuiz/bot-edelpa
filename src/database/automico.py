""" Importaciones """
from discord.ext import commands
from src.database.conexion_basededatos import conexion_db
from src.database.procedimientos import ProcedimientosAlmacenados
from src.utils.funciones_utiles import (comprobar_hora, comprobar_largo, 
                            comprobar_mayor, obtener_hora, formatear_hora, 
                            formatear_fecha, create_embed)

procedimiento = ProcedimientosAlmacenados()

class AlertaAutomatica():
    async def cambiar_estado_alerta(self, id:int) -> None:
        """Funcion que executa un procedimiento almacenado que apaga las alarmas,
        se ejecutará despues de que no haya intentos a realizar `self.auto_alertas()`"""
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC APAGAR_ALERTAS {id}"
                    await cursor.execute(query)

        except Exception as ex:
                print(f'Otro error: {ex}')


    async def bajar_contador_alertas(self, id: int) -> None:
        """Funcion para bajar el contador de veces que se debe executar una alerta"""
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC BAJAR_CONTADOR_ALERTA {id}"
                    await cursor.execute(query)

        except Exception as ex:
                print(f'error: {ex}')


    async def auto_alertas(self, bot: commands.Bot) -> None:
        """
        Funcion que esta en un ciclo `While True`, trae alertas y las muestra de forma automatica para que los usuarios 
        se den cuenta que hay un error en el robot o alguna area.
        """
        while True:
            lista_alertas = await procedimiento.obtener_alertas()

            if comprobar_largo(lista_alertas):
                for data in lista_alertas:
                    hora_data, hora_actual = formatear_hora(data[2]), formatear_hora(obtener_hora())
                    if comprobar_mayor(data[5]) is True and \
                        comprobar_hora(hora_data, hora_actual) is True:

                        channel = bot.get_channel(int(data[3]))
                        embed = create_embed(
                                        title=f'{data[0]}', description=f'{data[1]}', color=0x00ff00,
                                        author={'name':f'{bot.user.name}','url':'https://www.edelpa.cl/','icon_url':f'{bot.user.avatar.url}'},
                                        footer={'text':'Envases del Pacifico - Edelpa'}, 
                                        fields=[{'name':'Tiempo ocurrido', "value":f'{formatear_fecha(data[8])} | {formatear_hora(data[8])}', 'inline':False,}
                                                ,{'name':'Hora recordatorio', "value":f'{hora_data}', 'inline':False,}
                                                ,{'name':'id de Alerta', 'value':f'{data[4]}', 'inline':False,}
                                                ,{'name':'Cantidad de recordatorio', 'value':f'{data[5]}', 'inline':False}])

                        await channel.send(embed=embed)
                        await procedimiento.bajar_contador_alertas(int(data[4]))

                    elif comprobar_mayor(data[5]) is False:
                        await procedimiento.cambiar_estado_alerta(data[4])

                    else:
                        continue

            else:
                continue
