# import clase 
from src.Help.mensaje_ayuda import CustomHelpCommand
from discord.ext.commands.errors import ExtensionNotLoaded
# import discord
from discord.ext import commands
from discord import Intents
from discord import Game
from src.database.automico import AlertaAutomatica
#constantes
from src.config.config import TOKEN
# funciones
from src.utils.funciones_utiles import create_embed


def app_factory():
    alerta_automatica = AlertaAutomatica()
    descripcion = """Bot encargado de automatizar procesos e intentar """

    # Atributos
    intents = Intents.all()
    intents.message_content = True

    # Instancia Bot
    bot = commands.Bot(command_prefix='!', description=descripcion,
                       intents=intents, help_command = CustomHelpCommand())

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=Game(name="Working in Edelpa S.A."))
        bot.loop.create_task(alerta_automatica.auto_alertas(bot))
        print('Bot listo')

    return bot


bot = app_factory()


@bot.command()
async def sincronizar(ctx):
    try:
        await bot.tree.sync()
        await bot.reload_extension('src.comandos.comandos_menu')
        await bot.reload_extension('src.comandos.comandos')
        await bot.reload_extension('src.events.eventos')
        await bot.reload_extension('src.slash_comandos.slash')
        await ctx.send('Comandos actualizados')

    except Exception as ex:
        if isinstance(ex, ImportError):
            embed = create_embed(title='Error', description='Hubo un error al recargar las extensiones, verificar path de las extesiones.')
            await ctx.send(embed=embed)

        elif isinstance(ex, ExtensionNotLoaded):
            embed = create_embed(title='Error', description='Comandos no pudieron ser cargados y actualizados')
            await ctx.send(embed=embed)


async def run_bot():
    async with bot:
        await bot.load_extension('src.comandos.comandos_menu')
        await bot.load_extension('src.comandos.comandos')
        await bot.load_extension('src.events.eventos')
        await bot.load_extension('src.slash_comandos.slash')
        await bot.start(TOKEN)