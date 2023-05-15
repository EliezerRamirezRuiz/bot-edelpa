# import clase ayuda
from src.Help.mensaje_ayuda import CustomHelpCommand
# import discord
from discord.ext.commands.errors import ExtensionNotFound, ExtensionNotLoaded
from discord.ext import commands
from discord import Intents
from discord import Game
from src.database.automico import AlertaAutomatica


def app_factory():
    alerta_automatica = AlertaAutomatica()
    descripcion = """Bot encargado de automatizar procesos e intentar """

    # Atributos
    intents = Intents.all()
    intents.message_content = True

    # Instancia Bot
    bot = commands.Bot(command_prefix='!', description=descripcion,
                       intents=intents, help_command = CustomHelpCommand())


    async def cargar_extensiones():
        try:
            await bot.load_extension('src.comandos.comandos_menu')
            await bot.load_extension('src.comandos.comandos')
            await bot.load_extension('src.events.eventos')
            await bot.load_extension('src.slash_comandos.slash')
            print('extensiones cargadas')

        except Exception as ex:
            if isinstance(ex, ExtensionNotFound):
                print(f'Extension no encontrada')

            else:
                print(f'Error, contacte con el programador: {ex}')

    
    @bot.command()
    async def sincronizar(ctx):
        try:
            await bot.reload_extension('src.comandos.comandos_menu')
            await bot.reload_extension('src.comandos.comandos')
            await bot.reload_extension('src.events.eventos')
            await bot.reload_extension('src.slash_comandos.slash')
            await ctx.send('Comandos actualizados')

        except Exception as ex:
            if isinstance(ex, ImportError):
                await ctx.send('Hubo un error al recargar las extensiones, verificar path de las extesiones.')

            elif isinstance(ex, ExtensionNotLoaded):
                await cargar_extensiones()
                await ctx.send('Comandos cargados y actualizados')


    @bot.event
    async def on_ready():
        await bot.change_presence(activity=Game(name="Working in Edelpa S.A."))
        bot.loop.create_task(alerta_automatica.auto_alertas(bot))
        bot.loop.create_task(cargar_extensiones())
        print('Bot listo')


    return bot
