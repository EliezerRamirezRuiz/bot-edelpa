from discord import app_commands, Interaction  # im using discord.py rewrite(2.0.0)
from discord.ext.commands import Bot, Cog
from src.utils.funciones_utiles import mensaje_simple


class SlashComandos(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    @app_commands.command(name='slash_menu', description='Funcion para ejecutar el menú')
    async def slash_menu(self, interaccion: Interaction) -> None:
        Embed = mensaje_simple('Ejecutando menu...')
        await interaccion.response.send_message(embed=Embed)
        original_mensaje = await interaccion.original_response()  
        contexto = await self.bot.get_context(original_mensaje)

        comando = self.bot.get_cog('ComandosMenu')
        if comando is not None:
            await comando.menu(contexto)

    
    @app_commands.command(name='consultar_stock', description='slash comando')
    @app_commands.describe(codigo='Código a buscar, porfavor verificar código bien antes de escribirlo')
    async def consultar_stock(self, interaccion: Interaction, codigo:str) -> None:
        await interaccion.response.send_message(f'código:{codigo}')


    @app_commands.command(name='ultimas_alertas', description='slash comando')
    async def ultimas_alertas(self, interaccion: Interaction, codigo:str) -> None:
        await interaccion.response.send_message(f'codigo:{codigo}')


    @Cog.listener()
    async def on_ready(self):
        print('slash.py online.')



async def setup(bot):
    await bot.add_cog(SlashComandos(bot))
