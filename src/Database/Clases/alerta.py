""" Importaciones """
from discord import Embed
from Database.database import conexion_db


class Alerta():
    """
    Clase se encarga de las alertas y contendra todos los metodos que tengan alguna relacion con
    las alertas que sean llamados de comandos o menus con opciones
    """
    
    async def ultimas_alertas(self) -> None:
        """ Funcion que trae las ultimas alertas """
        try:
            conn = await conexion_db()
            async with conn.cursor() as cursor:
                query = f" EXEC ULTIMAS_ALERTAS "
                await cursor.execute(query)
                row = await cursor.fetchall()

        except Exception as ex:
            print(f'ultimas alerta :{ex}')

        else:
            if row is None:
                return []
                
            return row 
        
        finally:
            await cursor.close()
            await conn.close()

    
    async def ultimas_alertas_activas(self) -> Embed:
        """Funcion que trae los datos de la funcion `ultimas_alertas()`
        se manipulan para presentar y entregar de una manera mas 
        ordenada. En caso que no contenga alertas activas se mandara 
        un mensaje que le informe al usuario que no hay alertas"""

        data = await self.ultimas_alertas()
        
        if len(data) > 0:
            embed = Embed(title='Ultimas alertas activas', url='https://www.edelpa.cl/')
            embed.set_footer(text='Bot Edelpa S.A.')
            embed.set_image(url='https://raw.githubusercontent.com/EliezerEdelpa/Imagenes-Edelpa/main/foto_edelpa.png')
            
            for i in data:
                problema = i[0]
                error = i[1]
                fecha = i[3].strftime(r"%Y-%m-%d")
                hora = i[3].strftime(r"%H:%M:%S")
                estado = 'Activo' if i[2] == True else 'Desactivado'

                embed.add_field(name=f'PROBLEMA :{problema}',
                                value=f'''*ERROR: {error}
                                *Fecha: {fecha}
                                *Hora: {hora}
                                *Estado: {estado}''',
                                inline=False)
            
            return embed
        
        else:
            
            embed = Embed(title='No hay alertas activas')
            embed.set_footer(text='Bot Edelpa S.A.')
            return embed


    async def ultimas_alertas_desactivadas(self) -> Embed:
        """Funcion que trae los datos de la funcion `ultimas_alertas()`
        se manipulan para presentar y entregar de una manera mas 
        ordenada. En caso que no contenga alertas activas se mandara 
        un mensaje que le informe al usuario que no hay alertas"""

        embed = Embed(title="No se ha podido ultimas las ultimas alertas desactivadas")
        return embed