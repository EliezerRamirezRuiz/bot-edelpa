"""Archivo para controlar las alertas """
import discord
from Database.db import Database


class Alerta(Database):
    """Subclase heredada de Database, se encarga de las alertas 
    y contendra todos los metodos que tengan alguna relacion con
    las alertas que sean llamados de comandos o menus con opciones
    programables"""

    def __init__(self) -> None:
        super().__init__()


    async def get_data(self):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto muchas alertas. Todo a traves de un 
        procedimiento almacenado en caso de no contener datos se mandara
        una lista vacia [] """

        try:
            conn = await self.connection_sqlserver()
            async with conn.cursor() as cursor:
                query = f" EXEC ULTIMAS_ALERTAS "
                await cursor.execute(query)
                row = await cursor.fetchall()

                print(f'{row}\n -----------------------------------')
                if row is None:
                    return []
                
                return row 

        except Exception as ex:
            print(f'obtener alerta :{ex}')

        finally:
            await cursor.close()
            await conn.close()

    
    async def ultimas_alertas_activas(self):
        """Funcion que trae los datos de la funcion `get_data()`
        se manipulan para presentar y entregar de una manera mas 
        ordenada. En caso que no contenga alertas activas se mandara 
        un mensaje que le informe al usuario que no hay alertas"""

        data = await self.get_data()
        
        if len(data) > 0:
            embed = discord.Embed(title='Ultimas alertas activas', 
                                  url='https://www.edelpa.cl/')
            embed.set_footer(text='Bot Edelpa S.A.')
            embed.set_image(url='https://raw.githubusercontent.com/EliezerEdelpa/Imagenes-Edelpa/main/foto_edelpa.png')
            for i in data:
                problema = i[0]
                error = i[1]
                fecha = i[3].strftime(r"%Y-%m-%d")
                hora = i[3].strftime(r"%H:%M:%S")
                estado = 'Activo' if i[2] == True else 'Desactivado'

                embed.add_field(name=f'PROBLEMA :{problema}'
                                ,value=f'''*ERROR: {error}
                                *FECHA: {fecha}
                                *HORA: {hora}
                                *ESTADO: {estado}''',
                                inline=False)
            
            return embed
        
        else:
            
            embed = discord.Embed(title='No hay alertas activas')
            embed.set_footer(text='Bot Edelpa S.A.')
            return embed



