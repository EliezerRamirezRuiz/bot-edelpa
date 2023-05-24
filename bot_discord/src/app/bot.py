# import clase 
from src.database.automico import AlertaAutomatica
from src.ayuda.ayuda import CustomHelpCommand
# funciones
from src.server.webserver import peticion_server
# Loggers
from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO
# import discord
from discord.ext import commands
from discord import Intents
from discord import Game



def app_factory():
    alerta_automatica = AlertaAutomatica()
    descripcion = """Bot encargado de automatizar consultas y procesos"""

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
        bot.loop.create_task(peticion_server())
        my_handler.emit(makeLogRecord(
            {'msg': f"Bot listo", 
             'levelno': INFO, 
             'levelname':'INFO'}))

    return bot


bot = app_factory()


