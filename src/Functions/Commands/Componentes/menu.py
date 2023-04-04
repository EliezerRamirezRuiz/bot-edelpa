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
            label="Ultimas Alertas",
            description="Saber la cantidad de Bobinas que contiene un pallet",
            value="Ultimas Alertas"),
            
            discord.SelectOption(
            label="Reporte del dia",
            description="Saber la cantidad hecha por dia",
            value="Reporte del dia"),
            
            discord.SelectOption(
            label="prueba",
            description="Saber la cantidad hecha por dia",
            value="prueba"),]
        
        super().__init__(custom_id="Menu", placeholder="Menu",
                        min_values=1, max_values=1,
                        options=options, row=2)

    async def callback(self, interaccion:discord.Interaction):
        if self.values[0] == "prueba":
            message = await self.bot_command.stock(self.ctx)
            await self.ctx.send(message)
        if self.values[0] == "Consultar Stock":
            await self.bot_command.stock(self.ctx)


        elif self.values[0] == "Estado Robot":
            pass

        
        elif self.values[0] == "Ultimas Alertas":
            await self.bot_command.ultimas_alertas(self.ctx)


        elif self.values[0] == "Reporte del dia":
            await self.bot_command.ultimas_alertas(self.ctx)

