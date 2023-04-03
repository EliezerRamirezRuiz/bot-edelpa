from discord.ui import Select
import discord


class Menu(Select):
    def __init__(self, bot, ctx, bot_command):
        self.bot = bot
        self.ctx = ctx
        self.bot_command = bot_command

        options = [
            discord.SelectOption(
            label="Default",
            description="default",
            default=True,
            value="Default"),

            discord.SelectOption(
            label="Consultar Stock",
            description="Consultar stock de producto X",
            value="Consultar Stock"),

            discord.SelectOption(
            label="Estado Robot",
            description="Saber el estado actual del robot",
            value="Estado Robot"),

            discord.SelectOption(
            label="Ultimas alertas",
            description="Saber la cantidad de Bobinas que contiene un pallet",
            value="Option 3"),
            
            discord.SelectOption(
            label="Reporte del dia",
            description="Saber la cantidad hecha por dia",
            value="Reporte del dia"),]
        
        super().__init__(custom_id="Menu",
                         placeholder="Menu",
                         min_values=1,
                         max_values=1,
                         options=options
                         )

    async def callback(self):
        if self.values[0] == "Consultar Stock":
            await self.bot_command.stock(self.ctx)
            

        elif self.values[0] == "Estado Robot":
            await self.bot_command.estado_robot(self.ctx)

        
        elif self.values[0] == "Ultimas alertas":
            await self.bot_command.ultimas_alertas(self.ctx)
