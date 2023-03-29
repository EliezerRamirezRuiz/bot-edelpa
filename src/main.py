"""library used - All are in requirements.txt"""
import os
import logging
import discord

from dotenv import load_dotenv

from discord.ext import commands
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
bot = commands.Bot(command_prefix='!', description=descripcion,
                   intents=intents, help_command=CustomHelpCommand())


"""Configuration Bot"""
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='r+')



@bot.event
async def on_ready():
    """Function when the Bot is ready to answer commands"""
    await bot.add_cog(MyEvents(bot))
    await bot.add_cog(MyCommand(bot))
    print(f"Hello user {bot.user.name}")



def main():
    """Function to run the Bot"""
    try:
        bot.run(token=token)

    except Exception as error:
        print(f'error: {error}\nerror cause: {error.__cause__}')


if '__main__' == __name__:
    main()
