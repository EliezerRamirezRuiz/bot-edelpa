""" Instancia del bot, configuracion del bot, metodo para iniciar el bot y capturar excepciones"""
from src.Help.mensaje_ayuda import CustomHelpCommand
from discord.ext.commands.errors import ExtensionNotFound

from discord.ext import commands
from discord import Intents
from discord import Game


# instancia
from src.database import instancia_automatica


def app_factory():
    descripcion = """Bot encargado de automatizar consultas de alertas, reportes y stock"""

    """ Obligatory to retry connection"""
    intents = Intents.all()
    intents.message_content = True

    """ Instance Bot """
    bot = commands.Bot(command_prefix='!', description=descripcion,
                       intents=intents, help_command=CustomHelpCommand())


    async def cargar_extensiones():
        try:
            await bot.load_extension('src.comandos.comandos_menu')
            await bot.load_extension('src.comandos.comandos')
            await bot.load_extension('src.events.eventos')
            await bot.load_extension('src.slash_comandos.slash')
            print('extensiones cargadas')

        except Exception as ex:
            if isinstance(ex, ExtensionNotFound):
                print(f'error: {ex}')
            else:
                print(f'error: {ex}')

    
    @bot.command()
    async def sincronizar(ctx):
        try:
            await bot.reload_extension('src.comandos.comandos_menu')
            await bot.reload_extension('src.comandos.comandos')
            await bot.reload_extension('src.events.eventos')
            await bot.reload_extension('src.slash_comandos.slash')   
            await ctx.send('recarga lista listo')

        except ImportError:
            await ctx.send('Hubo un error al recargar las extensiones')


    @bot.event
    async def on_ready():
        await cargar_extensiones()
        await bot.change_presence(activity=Game(name="Working hard"))
        bot.loop.create_task(instancia_automatica.auto_alertas(bot))
        print('listo')

    return bot
