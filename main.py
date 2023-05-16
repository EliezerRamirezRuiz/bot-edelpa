from discord.ext.commands.errors import ExtensionNotLoaded
#constantes
from src.config.config import TOKEN
#funcion
from src.app.bot import app_factory
from src.server.webserver import keep_alive
# logging
import logging
import asyncio

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='r+')
bot = app_factory()


@bot.command()
async def sincronizar(ctx):
    try:
        await bot.reload_extension('src.comandos.comandos_menu')
        await bot.reload_extension('src.comandos.comandos')
        await bot.reload_extension('src.events.eventos')
        await bot.reload_extension('src.slash_comandos.slash')
        await ctx.send('Comandos actualizados')

    except Exception as ex:
        if isinstance(ex, ImportError):
            await ctx.send('Hubo un error al recargar las extensiones, verificar path de las extesiones.')

        elif isinstance(ex, ExtensionNotLoaded):
            await ctx.send('Comandos no pudieron ser cargados y actualizados')


async def main() -> None:
    """ Funcion para que el bot pueda correr y ante cualquier 
    inconveniente mande una excepecion expecion """
    try:
        #keep_alive()
        async with bot:
            await bot.load_extension('src.comandos.comandos_menu')
            await bot.load_extension('src.comandos.comandos')
            await bot.load_extension('src.events.eventos')
            await bot.load_extension('src.slash_comandos.slash')
            await bot.start(TOKEN)
        
    except Exception as ex:
        raise ex
    

if __name__ == '__main__':
    asyncio.run(main())

