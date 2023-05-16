# import clase ayuda
from src.Help.mensaje_ayuda import CustomHelpCommand
# import discord
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

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=Game(name="Working in Edelpa S.A."))
        bot.loop.create_task(alerta_automatica.auto_alertas(bot))
        print('Bot listo')


    return bot