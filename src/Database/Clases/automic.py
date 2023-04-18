import discord
import asyncio

from Database.db import Database


class AutomaticAlerta(Database):
    async def get_data(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto muchas alertas, todo a traves de un 
        procedimiento almacenado"""

        try:
            conn = await self.connection_sqlserver()
            async with conn.cursor() as cursor:
                query = f" EXEC MANDAR_ALERTAS "
                await cursor.execute(query)
                row = await cursor.fetchall()

                print(row)
                return row

        except Exception as ex:
            print(f'obtener alerta :{ex}')

        finally:
            await cursor.close()
            await conn.close()

    
    async def auto_alertas(self, bot):
        """Cada cierto tiempo trae alertas y las muestra de forma automatica para
        que los usuarios se den cuenta que hay un error en el robot o alguna area"""

        while True:
            await asyncio.sleep(60)
            lista_alertas = await self.get_data()

            if len(lista_alertas) == 0:
                print('no hay alertas')
                continue
            
            else:
                for data in lista_alertas:
                    # reemplaza channel_id con la ID del canal
                    channel = bot.get_channel(int(data[3])) 
                    embed = discord.Embed(title=f" {data[0]}", 
                                      description=f"{data[1]}", 
                                      color=0x00ff00)
                    
                    embed.set_author(name='Bot Edelpa - Alert!')
                    embed.set_footer(text='Empresa Edelpa S.A.')
                    embed.set_image(url='https://raw.githubusercontent.com/EliezerEdelpa/Imagenes-Edelpa/main/foto_edelpa.png')

                    await channel.send(embed=embed)