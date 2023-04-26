"""
Modulo encargado de mandar alertas automaticamente

Estado: Completado
"""
#import
import asyncio
#from through from
from discord.ext import commands
from discord import Embed
from Database.database import (conexion_db, comprobar_hora, 
                               comprobar_largo, comprobar_mayor)


class AutomaticAlerta():
    """Clase se enfoca en realizar acciones para las alertas automaticas"""
    async def get_data(self) -> list:
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
            await asyncio.sleep(15)
            lista_alertas = await self.get_data()

            if comprobar_largo(lista_alertas):

                for data in lista_alertas:

                    if comprobar_mayor(data[5]):
                        print(data)
                        # reemplaza channel_id con la ID del canal
                        channel = bot.get_channel(int(data[3])) 
                        embed = Embed(title=f" {data[0]}", description=f"{data[1]}", color=0x00ff00)
                        embed.set_author(name='Bot Edelpa - Alert!', icon_url=r'https://github.com/EliezerEdelpa/Imagenes-Edelpa/blob/main/Dise%C3%B1o%20sin%20t%C3%ADtulo%20(1).png')
                        embed.set_footer(text='Empresa Edelpa S.A.')
                        #embed.set_image(url='https://raw.githubusercontent.com/EliezerEdelpa/Imagenes-Edelpa/main/foto_edelpa.png')

                        await channel.send(embed=embed)
                        await self.bajar_contador_alertas(int(data[4]))

                    else: 
                        await self.cambiar_estado_alerta(data[4]) 

            else:
                print('no hay alertas')
                continue
                    