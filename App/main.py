"""library used - All are in requirements.txt"""
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
from Help.help_message import CustomHelpCommand
from Events.extends_events import MyEvents
from Commands.extends_commands import MyCommand


load_dotenv()


"""Variables"""
token = os.environ["BOT_SECRET_TOKEN"]


"""configuration"""
descripcion = """Hola soy el bot de Edelpa S.A, \nte ayudare a enterarte de las alertas mas recientes del robot."""


""" Intents iy's going to connect to discord, is Obligatory"""
intents = discord.Intents.default()
intents.message_content = True


""" Instance Bot """
bot = commands.Bot(command_prefix='!', description=descripcion, intents=intents)
bot.help_command = CustomHelpCommand()


@bot.event
async def on_ready():
    """function when the Bot is started"""
    await bot.add_cog(MyEvents(bot))
    await bot.add_cog(MyCommand(bot))
    print(f"Hello users {bot.user}") 
    

def main():
    """function to run the Bot"""
    try:
        bot.run(token=token)
    except Exception as error:
        print(f'error: {error}\nerror.__cause__: {error.__cause__}')


if '__main__' == __name__:
    main()
