#constantes
from src.config.config import TOKEN

#funcion
from src.app.bot import app_factory

# logging
import logging


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='r+')
bot = app_factory()


def main() -> None:
    """ Funcion para que el bot pueda correr y ante cualquier 
    inconveniente mande una excepecion expecion """
    try:
        bot.run(TOKEN,  log_handler=handler)
        
    except Exception as ex:
        raise ex
    

if __name__ == '__main__':
    main()

