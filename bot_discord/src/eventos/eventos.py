from discord.ext.commands import CommandNotFound, MissingRequiredArgument, DisabledCommand
from discord.ext.commands import Cog, Bot

from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO, WARNING


class MyEvents(Cog):
    def __init__(self, bot):
        self.bot = bot


    @Cog.listener()
    async def on_message(self, message):
        my_handler.emit(makeLogRecord({'msg': f"{message.author.name} sent a message: {message.content} ", 
                                       'levelno': INFO, 'levelname':'INFO'}))


    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send('Comando no encontrado. Para saber mas de los comandos, porfavor ejecute !help')

        elif isinstance(error, MissingRequiredArgument):
            await ctx.send('Argumento no requerido no encontrado.')

        elif isinstance(error, DisabledCommand):
            await ctx.send('Este comando ha sido desabilitado')

        else:
            print(error)  # Print the error to the console
            await ctx.send('Ocurrio un error mientras se ejecuta el comando')


    @Cog.listener()
    async def on_command(self, ctx):
        my_handler.emit(makeLogRecord({'msg': f"Comando '{ctx.command.name}' fue usado por {ctx.author.name} # {ctx.author.discriminator}",
                                        'levelno': INFO, 'levelname':'INFO'}))


    @Cog.listener()
    async def on_command_completion(self, ctx):
        my_handler.emit(makeLogRecord({'msg': f"Comando '{ctx.command}' fue ejecutado exitosamente",
                                        'levelno': INFO, 'levelname':'INFO'}))


    @Cog.listener()
    async def on_connect(self):
        my_handler.emit(makeLogRecord({'msg': "Bot Trabajando", 'levelno': INFO, 'levelname':'INFO'}))

    
    @Cog.listener()
    async def on_disconnect(self):
        my_handler.emit(makeLogRecord({'msg': "Bot apagado", 'levelno': WARNING, 'levelname':'WARNING'}))
    

    @Cog.listener()
    async def on_member_join(self, member):
        my_handler.emit(makeLogRecord({'msg': f"{member} ha entrado al servidor", 'levelno': INFO, 'levelname':'INFO'}))


    @Cog.listener()
    async def on_member_remove(self, member):
        my_handler.emit(makeLogRecord({'msg': f"{member} ha salido del servidor", 'levelno': INFO, 'levelname':'INFO'}))
    

    @Cog.listener()
    async def on_member_join(self, member):
        # Obtener el canal de bienvenida del servidor
        welcome_channel = member.guild.system_channel()
        if welcome_channel is not None:
            # Enviar mensaje de bienvenida
            await welcome_channel.send(f'Bienvenido {member.mention} al servidor!')

    @Cog.listener()
    async def on_ready(self):
        my_handler.emit(makeLogRecord({'msg': f"eventos.py online.", 'levelno': INFO, 'levelname':'INFO'}))
        

async def setup(bot:Bot):
    await bot.add_cog(MyEvents(bot))
    my_handler.emit(makeLogRecord({'msg': "He sido cargado eventos.py", 'levelno': INFO, 'levelname':'INFO'}))


async def teardown(bot:Bot):
    await bot.remove_cog(MyEvents(bot))
    my_handler.emit(makeLogRecord({'msg': "Ha sido descargado eventos.py!", 'levelno': INFO, 'levelname':'INFO'}))
    
