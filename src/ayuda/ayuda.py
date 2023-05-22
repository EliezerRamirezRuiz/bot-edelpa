from discord.ext.commands import MinimalHelpCommand
from src.utils.funciones_utiles import create_embed

class CustomHelpCommand(MinimalHelpCommand):
    def __init__(self):
        super().__init__(no_category="No categorizado")


    def get_opening_note(self):
        return  '''Nota: cada comando esta detallado y escrito de forma explicita'''


    def get_ending_note(self):
        return ''' Contacte con `{Area de informática}` para mas ayuda.'''


    async def send_pages(self):
        encabezado = self.get_opening_note()
        pie_de_pagina = self.get_ending_note()
        embed = create_embed(
                    title=f'Comando !help', description=f'{encabezado}', color=0x00ff00,
                    author={'name':f'{self.context.bot.user.name}','url':'https://www.edelpa.cl/','icon_url':f'{self.context.bot.user.avatar.url}'},
                    footer={'text':pie_de_pagina}, 
                    fields=[
                        {'name':'COMANDOS (Comando de invocación [`!`])',
                         "value":f"""
                            -menu (Opciones)
                            -consultar_stock (parametro: codigo[int])
                            -estado_robot (sin parametros)(pendiente)
                            -alertas_activa (sin parametros)
                            -alertas_desactivadas (sin parametros)
                            -sincronizar (Recarga las extensiones)
                            -help""", 
                         'inline':False,}
                        ,{'name':'OPCIONES MENU (Comando de invocación [`!menu` | `/menu`])',
                          "value":f"""
                            -Default 
                            -Consultar stock 
                            -Estado robot
                            -Ultimas alertas activas
                            -Ultimas alertas desactivadas
                            -Reporte del dia""", 
                          'inline':False,}
                            ,{'name':'COMANDOS SLASH (Comando de invocación [`/`])',
                              'value':f"""
                                -menu
                                -consultar_stock (parametro: codigo[int])
                                -ultimas_alertas_activas
                                -ultimas_alertas_desactivadas
                                -estado_robot`""", 
                              'inline':False,}])        

        await self.get_destination().send(embed=embed)
  
