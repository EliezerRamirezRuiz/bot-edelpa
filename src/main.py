from Database.Clases import alerta_automatica
from Events.eventos import MyEvents
from Commands.comandos.discord_menu import MenuCommands
from Commands.comandos.get_commands import GetCommands
from discord import Game

from src.app.bot import app
from src.config.config import TOKEN

# Import
import logging



"""Configuration Bot"""
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='r+')

bot = app()


@bot.event
async def on_ready():
    """Evento que esta disponible cuando el bot se conecta de manera correcta \n
    y realiza el registro de las subclases de de Commands.cog, para que esten \n
    disponible los comandos anidados"""
    await bot.add_cog(MyEvents(bot))
    await bot.add_cog(MenuCommands(bot))
    await bot.add_cog(GetCommands(bot))
    await bot.change_presence(activity=Game(name="Working hard"))
    bot.loop.create_task(alerta_automatica.auto_alertas(bot))


def main() -> None:
    """ Funcion para que el bot pueda correr y ante cualquier 
    inconveniente mande una excepecion expecion """
    try:
        bot.run(TOKEN)
        
    except Exception as ex:
        raise ex
    

if __name__ == '__main__':
    main()