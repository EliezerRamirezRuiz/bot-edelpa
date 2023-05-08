from discord.ext import commands
from discord.ui import View
from discord import Interaction

from componentes.menu_ctx import Menu


class ComandosMenu(commands.Cog):
    """Aqui se define una clase con metodos que son 
    comandos que solo pueden ser llamadas por el menu"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def menu(self, ctx):
        """Menu con opciones, las opciones son funciones que  
        posteriormente podrian requerir respuesta del usuario"""
        select = Menu(self.bot, ctx)
        view = View(timeout=180)
        view.add_item(select)
        await ctx.send(view=view)