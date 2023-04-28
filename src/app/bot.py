""" Instancia del bot, configuracion del bot, metodo para iniciar el bot y capturar excepciones"""
from src.Help.mensaje_ayuda import CustomHelpCommand
from discord.ext import commands
from discord import Intents


def app():
    descripcion = """Bot encargado de automatizar consultas de alertas, reportes y stock"""

    """ Obligatory to retry connection"""
    intents = Intents.default()
    intents.message_content = True

    """ Instance Bot """
    bot = commands.Bot(command_prefix='!', description=descripcion, intents=intents, help_command=CustomHelpCommand())
    return bot



    
