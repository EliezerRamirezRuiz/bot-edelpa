from discord.ext.commands import MinimalHelpCommand
from src.utils.funciones_utiles import create_embed

class CustomHelpCommand(MinimalHelpCommand):
    def __init__(self):
        super().__init__(no_category="Sin categoria")


    async def send_command_help(self, command):
        # This method is called if a specific command is requested in the help command
        # We can customize the message that is sent here
        message = f'''  Ayuda para comandos {command}: {command.help}\n  
                        Funciones para comandos '''
        await self.get_destination().send(message)
