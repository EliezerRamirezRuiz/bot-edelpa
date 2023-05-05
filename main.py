#constantes
from src.config.config import TOKEN

#instancia
from src.database import instancia_automatica

#clase
from src.comandos.discord_menu import ComandosMenu
from src.comandos.comandos import ComandosPrincipales
from src.Events.eventos import MyEvents

#funcion
from src.app.bot import app
from discord import Game

# module
from discord import Interaction
import logging


"""Configuration Bot"""
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='r+')


bot = app()


@bot.tree.command(name='menu', description='Invocamos el comando menu para poder llamar otras funciones',  extras={'Command':'menu'})
async def slash_menu(interaction: Interaction):
    await interaction.response.send_message('Hola', ephemeral=True)


@bot.command()
async def sincronizar(ctx):
    await bot.tree.sync()
    await ctx.send('comandos slashes actualizado')


@bot.event
async def on_ready():
    """Evento que esta disponible cuando el bot se conecta de manera correcta \n
    y realiza el registro de las subclases de de Commands.cog, para que esten \n
    disponible los comandos anidados"""
    await bot.add_cog(MyEvents(bot))
    await bot.add_cog(ComandosMenu(bot))
    await bot.add_cog(ComandosPrincipales(bot))
    await bot.change_presence(activity=Game(name="Working hard"))
    bot.loop.create_task(instancia_automatica.auto_alertas(bot))


def main() -> None:
    """ Funcion para que el bot pueda correr y ante cualquier 
    inconveniente mande una excepecion expecion """
    try:
        bot.run(TOKEN)
        
    except Exception as ex:
        raise ex
    

if __name__ == '__main__':
    main()