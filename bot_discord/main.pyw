# discord
from discord.ext.commands.errors import ExtensionNotLoaded
# asyncio
from asyncio import TaskGroup, run
from logging import makeLogRecord
from logging import INFO, WARNING
# constantes
from src.config.config import TOKEN
# aplicacion
from src.app.bot import bot
from src.utils.funciones_utiles import create_embed
from src.server.webserver import run_server
from src.logger.logger_app import my_handler
# import
import time


@bot.command()
async def sincronizar(ctx):
    try:
        await bot.tree.sync()
        await bot.reload_extension('src.comandos.comandos_menu')
        await bot.reload_extension('src.comandos.comandos')
        await bot.reload_extension('src.eventos.eventos')
        await bot.reload_extension('src.slash_comandos.slash')
        await ctx.send('Comandos actualizados')

    except Exception as ex:
        my_handler.emit(makeLogRecord(
            {'msg': f'''Ocurrio el siguiente error: {ex}''',
            'levelno': WARNING,
            'levelname':'WARNING'})) 
        if isinstance(ex, ImportError):
            embed = create_embed(title='Error', description='Hubo un error al recargar las extensiones, verificar path de las extesiones.')
            await ctx.send(embed=embed)

        elif isinstance(ex, ExtensionNotLoaded):
            embed = create_embed(title='Error', description='Comandos no pudieron ser cargados y actualizados')
            await ctx.send(embed=embed)
        
        else:
            embed = create_embed(title='Error', description='Error durante el proceso de sincronizacion')
            await ctx.send(embed=embed)            


async def run_bot():
    async with bot:
        await bot.load_extension('src.comandos.comandos_menu')
        await bot.load_extension('src.comandos.comandos')
        await bot.load_extension('src.eventos.eventos')
        await bot.load_extension('src.slash_comandos.slash')
        await bot.start(TOKEN)


async def main() -> None:
    try:
        async with TaskGroup() as tg:
            task2 = tg.create_task(run_server())
            task1 = tg.create_task(run_bot())
            my_handler.emit(makeLogRecord(
                {'msg': f"started at {time.strftime('%X')}", 
                 'levelno': INFO, 
                 'levelname':'INFO'}))

    except ExceptionGroup as ex:
        my_handler.emit(makeLogRecord(
            {'msg': f'''Ocurrio el siguiente error: {ex.with_traceback()},
            {ex.__class__},
            {ex.__context__}''',
            'levelno': WARNING,
            'levelname':'WARNING'}))        
    

if __name__ == '__main__':
    run(main())