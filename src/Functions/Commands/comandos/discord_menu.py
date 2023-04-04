from discord.ext import commands
from discord.ui import View

from Functions.Commands.Componentes.menu import Menu
from Functions.Commands.Database.Funciones.funciones_db import \
    obtener_stock, estado_del_robot, obtener_alerta, reporte_dia



class MenuCommands(commands.Cog):
    """Aqui se define una clase con metodos que son 
    comandos que solo pueden ser llamadas por el menu"""
    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    async def menu(self, ctx):
        """Menu con opciones, las opciones son funciones"""
        select = Menu(self.bot, ctx, self)
        view = View(timeout=180)
        view.add_item(select)
        await ctx.send(select.placeholder, view=view)
    

    @menu.command()
    async def stock(self, ctx):
        """Funcion consultar stock a pedir"""
        try:
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
            result = await obtener_stock(str(message.content), ctx)

            return result
        
        except Exception as ex:
            return f"stock : {ex}"


    @menu.command()
    async def estado_robot(self, ctx):
        """Funcion consultar estado del robot"""
        try:
            await ctx.send("Consultando estado del robot")
            result = await estado_del_robot(ctx)

            await ctx.send(result)

        except Exception as ex:
            await ctx.send(f"estado del robot: {ex}")


    @menu.command()
    async def ultimas_alertas(self, ctx):
        """Funcion consultar ultimas alertas"""
        try:
            await ctx.send("Obteniendo alertas")
            result = await obtener_alerta(ctx)

            await ctx.send(result)
        
        except Exception as ex:
            await ctx.send(f"ultimas alertas:{ex}")


    @menu.command()
    async def reporte_del_dia(self, ctx):
        """Funcion consultar reporte del dia
        condiciones a visualizar"""
        try:
            await ctx.send("Obteniendo reporte")
            result = await reporte_dia(ctx)

            await ctx.send(result)
        
        except Exception as ex:
            await ctx.send(f"ultimas alertas:{ex}")