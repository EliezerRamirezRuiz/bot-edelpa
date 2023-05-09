from discord import app_commands, Interaction  # im using discord.py rewrite(2.0.0)
from discord.ext.commands import Bot, Cog


class SlashComandos(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    @app_commands.command(name='menu', description='Funcion para ejecutar el menú')
    async def menu(self, interaccion: Interaction) -> None:
        await interaccion.response.send_message('Menu')
        original_mensaje = await interaccion.original_response()  
        contexto = await self.bot.get_context(original_mensaje)

        comando = self.bot.get_cog('ComandosMenu')
        if comando is not None:
            await comando.menu(contexto)

    
    @app_commands.describe(codigo='Codigo a buscar, porfavor verificar codigo bien antes de escribirlo')
    @app_commands.command(name='consultar_stock', description='slash comando')
    async def consultar_stock(self, interaccion: Interaction, codigo:str) -> None:
        await interaccion.response.send_message(f'codigo:{codigo}')

    

    @app_commands.command(name='ultimas_alertas', description='slash comando')
    async def consultar_stock(self, interaccion: Interaction, codigo:str) -> None:
        await interaccion.response.send_message(f'codigo:{codigo}')


    @Cog.listener()
    async def on_ready(self):
        print('slash.py online.')


async def setup(bot):
    await bot.add_cog(SlashComandos(bot))
