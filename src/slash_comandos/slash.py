from discord import app_commands, Interaction 
from discord.ext.commands import Bot, Cog
from src.utils.funciones_utiles import mensaje_simple


class SlashComandos(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    @app_commands.commands.command(name='slash_menu', description='Ejecuta el comando !menu')
    async def slash_menu(self, interaccion: Interaction) -> None:
        Embed = mensaje_simple('Procesando menu...')
        await interaccion.response.send_message(embed=Embed)
        original_mensaje = await interaccion.original_response()  
        contexto = await self.bot.get_context(original_mensaje)

        comando = self.bot.get_cog('ComandosMenu')
        if comando is not None:
            await comando.menu(contexto)

    
    @app_commands.command(name='consultar_stock', description='Ejecuta el comando !consultar_stock')
    @app_commands.describe(codigo="""Código requerido para buscar el stock, Ejemplo: 'EP100000000006000621850000500010'  """)
    async def consultar_stock(self, interaccion: Interaction, codigo:str) -> None:
        Embed = mensaje_simple('Procesando solicitud...')
        await interaccion.response.send_message(embed=Embed)
        original_mensaje = await interaccion.original_response()
        contexto = await self.bot.get_context(original_mensaje)

        comando = self.bot.get_cog('ComandosPrincipales')
        if comando is not None:
            await comando.consultar_stock(contexto, codigo)


    @app_commands.command(name='ultimas_alertas_activas', description='Trae las ultimas alertas desactivadas')
    async def alertas_activas(self, interaccion: Interaction) -> None:
        Embed = mensaje_simple('Procesando solicitud...')
        await interaccion.response.send_message(embed=Embed)
        original_mensaje = await interaccion.original_response()  
        contexto = await self.bot.get_context(original_mensaje)
        
        comando = self.bot.get_cog('ComandosPrincipales')
        if comando is not None:
            await comando.alertas_activas(contexto)


    @app_commands.command(name='ultimas_alertas_desactivadas', description='Trae las ultimas alertas desactivadas')
    async def alertas_desactivadas(self, interaccion: Interaction) -> None:
        Embed = mensaje_simple('Procesando solicitud...')
        await interaccion.response.send_message(embed=Embed)
        original_mensaje = await interaccion.original_response()  
        contexto = await self.bot.get_context(original_mensaje)
        
        comando = self.bot.get_cog('ComandosPrincipales')
        if comando is not None:
            await comando.alertas_desactivadas(contexto)


    @app_commands.command(name='estado_robot', description='Trae el estado de robot')
    async def estado_robot(self, interaccion: Interaction) -> None:
        Embed = mensaje_simple('Procesando solicitud...')
        await interaccion.response.send_message(embed=Embed)
        original_mensaje = await interaccion.original_response()  
        contexto = await self.bot.get_context(original_mensaje)
        
        comando = self.bot.get_cog('ComandosPrincipales')
        if comando is not None:
            await comando.estado_robot(contexto)


    @Cog.listener()
    async def on_ready(self):
        print('slash.py online.')


async def setup(bot:Bot):
    print('I am being loaded from slash.py')
    await bot.add_cog(SlashComandos(bot))
