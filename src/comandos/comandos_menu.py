from discord.ext.commands import Cog, Bot
from discord.ext.commands import command
from discord.ui import View

from src.componentes.menu import Menu


class ComandosMenu(Cog):
    """Aqui se define una clase con metodos que son 
    comandos que solo pueden ser llamadas por el menu"""
    def __init__(self, bot):
        self.bot = bot


    @command()
    async def menu(self, ctx):
        """Menu con opciones, las opciones son funciones que  
        posteriormente podrian requerir respuesta del usuario"""
        select = Menu(self.bot, ctx)
        view = View(timeout=180)
        view.add_item(select)
        await ctx.send(view=view)


    @Cog.listener()
    async def on_ready(self):
        print('Comandos_menu.py online.')


async def setup(bot:Bot):
    print('I am being loaded from comandos_menu.py')
    await bot.add_cog(ComandosMenu(bot))


async def teardown(bot:Bot):
    print('I am being unloaded from comandos_menu.py!')
    await bot.remove_cog(ComandosMenu(bot))