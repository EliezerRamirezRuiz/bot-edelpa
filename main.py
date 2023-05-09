#constantes
from src.config.config import TOKEN

#instancia
from src.database import instancia_automatica

#clase
"""from src.comandos.comandos_menu import ComandosMenu
from src.comandos.comandos import ComandosPrincipales
from src.Events.eventos import MyEvents
from src.slash_comandos.slash import SlashComandos"""

#funcion
from src.app.bot import app
from discord import Game

# logging
import logging


"""Configuration Bot"""
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='r+')


bot = app()


@bot.command()
async def cargar_extensiones(ctx):
    await bot.load_extension('src.comandos.comandos_menu')
    await bot.load_extension('src.comandos.comandos')
    await bot.load_extension('src.Events.eventos')
    await bot.load_extension('src.slash_comandos.slash')
    await ctx.send('carga lista')


@bot.command()
async def sincronizar(ctx):
    await bot.reload_extension('src.comandos.comandos_menu')
    await bot.reload_extension('src.comandos.comandos')
    await bot.reload_extension('src.Events.eventos')
    await bot.reload_extension('src.slash_comandos.slash')   
    await ctx.send('recarga lista listo')


@bot.event
async def on_ready():
    await bot.change_presence(activity=Game(name="Working hard"))
    bot.loop.create_task(instancia_automatica.auto_alertas(bot))
    print('listo')


def main() -> None:
    """ Funcion para que el bot pueda correr y ante cualquier 
    inconveniente mande una excepecion expecion """
    try:
        bot.run(TOKEN)
        
    except Exception as ex:
        raise ex
    

if __name__ == '__main__':
    main()

