from discord import app_commands # im using discord.py rewrite(2.0.0)
from discord.ext.commands import Bot, Cog
from discord import Interaction 


class SlashComandos(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.command(name='menu', description='Funcion para ejecutar el menú')
    async def menu(self, interaccion: Interaction) -> ...:
        ...

        


