from discord import app_commands, Interaction 
from discord.ext.commands import Bot, Cog
from discord.ui import View

from src.componentes.menu import Menu
from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO, WARNING


class SlashComandos(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    @app_commands.command(name='slash_menu', description='Ejecuta el comando !menu')
    async def slash_menu(self, interaccion: Interaction) -> None:
        ctx = await self.bot.get_context(interaccion)
        select = Menu(self.bot)
        view = View(timeout=180)
        view.add_item(select)
        await interaccion.response.send_message(view=view)

    
    @app_commands.describe(codigo="""Código requerido para buscar el stock, Ejemplo: 'EP100000000006000621850000500010'  """)
    @app_commands.command(name='consultar_stock', description='Ejecuta el comando !consultar_stock')
    async def consultar_stock(self, interaccion: Interaction, codigo:str) -> None:
        ctx = await self.bot.get_context(interaccion)
        comando = self.bot.get_cog('ComandosPrincipales')
        if comando is not None:
            await comando.consultar_stock(ctx, codigo)


    @app_commands.command(name='ultimas_alertas_activas', description='Trae las ultimas alertas desactivadas')
    async def alertas_activas(self, interaccion: Interaction) -> None:
        ctx = await self.bot.get_context(interaccion)
        comando = self.bot.get_cog('ComandosPrincipales')
        if comando is not None:
            await comando.alertas_activas(ctx)


    @app_commands.command(name='ultimas_alertas_desactivadas', description='Trae las ultimas alertas desactivadas')
    async def alertas_desactivadas(self, interaccion: Interaction) -> None:
        ctx = await self.bot.get_context(interaccion)
        comando = self.bot.get_cog('ComandosPrincipales')
        if comando is not None:
            await comando.alertas_desactivadas(ctx)


    @app_commands.command(name='estado_robot', description='Trae el estado de robot')
    async def estado_robot(self, interaccion: Interaction) -> None:
        ctx = await self.bot.get_context(interaccion)
        comando = self.bot.get_cog('ComandosPrincipales')
        if comando is not None:
            await comando.estado_robot(ctx)


    @Cog.listener()
    async def on_ready(self):
        my_handler.emit(makeLogRecord({'msg': f"slash.py online.", 'levelno': INFO, 'levelname':'INFO'}))


async def setup(bot:Bot):
    await bot.add_cog(SlashComandos(bot))
    my_handler.emit(makeLogRecord({'msg': f"I am being loaded from slash.py", 'levelno': INFO, 'levelname':'INFO'}))


async def teardown(bot:Bot):
    await bot.remove_cog(SlashComandos(bot))
    my_handler.emit(makeLogRecord({'msg': f"I am being unloaded from slash.py!", 'levelno': INFO, 'levelname':'INFO'}))