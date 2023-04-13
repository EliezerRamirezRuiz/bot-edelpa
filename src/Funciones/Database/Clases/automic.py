import discord

from Funciones.Database.db import Database


class Robot(Database):
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
        while True:
            lista_alertas = await self.get_data()

            if len(lista_alertas) == 0:
                print('no hay alertas')
                continue

            else:
                for data in lista_alertas:
                    channel = bot.get_channel(int(data[3])) # reemplaza channel_id con la ID del canal
                    embed = discord.Embed(title=f" {data[0]}", 
                                      description=f"{data[1]}", 
                                      color=0x00ff00)
                    
                    embed.set_author(name='Bot Edelpa - Alert!')
                    embed.set_footer(text='Empresa Edelpa S.A.')
                    embed.set_image(url=r'https://th.bing.com/th/id/R.0de9abb7e7be3ede39e3089766e1fb22?rik=5DsHUWcsUz204g&riu=http%3a%2f%2fwww.edelpa.cl%2fwp-content%2fuploads%2f2016%2f05%2flogoed-1.png&ehk=jKhlu77qPO4zrSLBdpJpGBA3tMeARHjaJFedyp2skqo%3d&risl=&pid=ImgRaw&r=0')

                    await channel.send(embed=embed)