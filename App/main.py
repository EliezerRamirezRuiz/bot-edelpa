"""library used - All are in requirements.txt"""
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

from Help.help_message import CustomHelpCommand
from Events.extends_events import MyEvents
from Commands.extends_commands import MyCommand


load_dotenv()


"""Variables"""
token = os.environ["BOT_SECRET_TOKEN"]
descripcion = """Hola soy el bot de Edelpa S.A, \nte ayudare a enterarte de las alertas mas recientes del robot."""


""" Obligatory to retry connection"""
intents = discord.Intents.default()
intents.message_content = True


""" Instance Bot """
bot = commands.Bot(command_prefix='!', description=descripcion, intents=intents)
bot.help_command = CustomHelpCommand() #Help/help_message.py


"""Configuration Bot"""



@bot.event
async def on_ready():
    """Function when the Bot is started"""
    await bot.add_cog(MyEvents(bot))
    await bot.add_cog(MyCommand(bot))
    print(f"Hello users {bot.user}") 
    

def main():
    """Function to run the Bot"""
    try:
        bot.run(token=token)
    except Exception as error:
        print(f'error: {error}\nerror.__cause__: {error.__cause__}')


if '__main__' == __name__:
    main()
