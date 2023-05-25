from discord.ext.commands import Cog, Bot
from discord.ext.commands import command
from discord.ui import View

from src.componentes.menu import Menu
from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO, WARNING


class ComandosMenu(Cog):
    """Aqui se define una clase con metodos que son 
    comandos que solo pueden ser llamadas por el menu"""
    def __init__(self, bot):
        self.bot = bot


    @command()
    async def menu(self, ctx):
        """Menu con opciones, las opciones son funciones que  
        posteriormente podrian requerir respuesta del usuario"""
        try:
            select = Menu(self.bot, ctx)
            view = View(timeout=180)
            view.add_item(select)
            await ctx.send(view=view)
        
        except Exception as ex:
            my_handler.emit(makeLogRecord({
                'msg': f"Ocurrio este error: {ex}", 
                'levelno': WARNING, 
                'levelname':'WARNING'}))
            await ctx.send('Ocurrio un error, contacte con el Areá TI')


    @Cog.listener()
    async def on_ready(self):
        my_handler.emit(makeLogRecord({
            'msg': f"Comandos_menu.py en linea.", 
            'levelno': INFO, 
            'levelname':'INFO'}))


async def setup(bot:Bot):
    await bot.add_cog(ComandosMenu(bot))
    my_handler.emit(makeLogRecord({
        'msg': f"He sido cargado comandos_menu.py", 
        'levelno': INFO, 
        'levelname':'INFO'}))    


async def teardown(bot:Bot):
    await bot.remove_cog(ComandosMenu(bot))
    my_handler.emit(makeLogRecord({
        'msg': f"He sido bajado comandos_menu.py!", 
        'levelno': INFO, 
        'levelname':'INFO'}))     