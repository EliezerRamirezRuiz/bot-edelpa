""" Importaciones """
from discord import Embed
from src.database.db import conexion_db


class Alerta():
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


    async def ultimas_alertas_activas(self) -> Embed:
        """Funcion que trae los datos de la funcion `alertas_activas()` se manipulan para presentar
        y entregar de una manera mas ordenada. En caso que no contenga alertas activas se mandara 
        un mensaje que le informe al usuario que no hay alertas"""

        data = await self.alertas_activas()
        
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