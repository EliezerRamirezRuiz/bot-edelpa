"""
Modulo encargado de mandar alertas automaticamente

Estado: Completado
"""
#import
import asyncio
from asyncio.exceptions import CancelledError
#from through from
from discord.ext import commands
from discord import Embed
from Database.database import (conexion_db, comprobar_hora, 
                               comprobar_largo, comprobar_mayor,
                               obtener_hora)


class AutomaticAlerta():
    """Clase se enfoca en realizar acciones para las alertas automaticas"""
    def __init__(self) -> None:
        pass
    

    async def obtener_alertas(self) -> list:
        """ Funcion para traer datos `{Procedure MANDAR_ALERTAS}` """
        try:
            conn = await conexion_db()
            async with conn.cursor() as cursor:
                query = f" EXEC MANDAR_ALERTAS "
                await cursor.execute(query)
                row = await cursor.fetchall()

        except Exception as ex:
            print(f'obtener alerta :{ex}')

        else:
            if row is None:
                return []
            return row

        finally:
            await cursor.close()
            await conn.close()


    async def cambiar_estado_alerta(self, id:int) -> None:
        """Funcion que executa un procedimiento almacenado que apaga las alarmas,
        se executara despues de haber mandado las alertas con la funcion `self.auto_alertas()`"""
        try:
            conn = await conexion_db()
            async with conn.cursor() as cursor:
                query = f" EXEC APAGAR_ALERTAS {id}"
                await cursor.execute(query)

        except Exception:
            await 'error al cambiar el estado de la alerta'

        finally:
            await cursor.close()
            await conn.close()


    async def bajar_contador_alertas(self, id:int) -> None:
        """Funcion para bajar el contador de veces que se debe executar una alerta"""
        try:
            conn = await conexion_db()
            async with conn.cursor() as cursor:
                query = f" EXEC BAJAR_CONTADOR_ALERTA {id}"
                await cursor.execute(query)

        except Exception:
            print('error al modificar alerta')

        finally:
            await cursor.close()
            await conn.close()
        
    
    async def auto_alertas(self, bot:commands.Bot) -> None:
        """Cada cierto tiempo trae alertas y las muestra de forma automatica para
        que los usuarios se den cuenta que hay un error en el robot o alguna area"""
        while True:
            lista_alertas = await self.obtener_alertas()
            if comprobar_largo(lista_alertas):
                for data in lista_alertas:
                    print(data[2], obtener_hora())
                    if comprobar_mayor(data[5]) == True and comprobar_hora(obtener_hora() ,data[2]) == True:
                        print(data)
                        # reemplaza channel_id con la ID del canal
                        channel = bot.get_channel(int(data[3])) 
                        embed = Embed(title=f" {data[0]}", description=f"{data[1]}", color=0x00ff00)
                        embed.set_author(name='Bot Edelpa - Alert!', icon_url=r'https://raw.githubusercontent.com/EliezerEdelpa/Imagenes-Edelpa/main/foto_edelpa.png')
                        embed.set_footer(text='Empresa Edelpa S.A.')
                        #embed.set_image(url='')
                        await channel.send(embed=embed)
                        await self.bajar_contador_alertas(int(data[4]))  
                    
                    else: 
                        await self.cambiar_estado_alerta(data[4]) 
            else:
                continue
                    