from discord.ext.commands import Cog, Bot
from discord.ext.commands import CommandNotFound, MissingRequiredArgument, DisabledCommand


class MyEvents(Cog):
    def __init__(self, bot):
        self.bot = bot


    @Cog.listener()
    async def on_message(self, message):
        print(f'{message.author.name} sent a message: {message.content}')


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
        print(f"Comando '{ctx.command.name}' fue usado por {ctx.author.name} # {ctx.author.discriminator}")


    @Cog.listener()
    async def on_command_completion(self, ctx):
        print(f"Comando '{ctx.command}' fue ejecutado exitosamente")


    @Cog.listener()
    async def on_connect(self):
        print("Bot Trabajando")

    
    @Cog.listener()
    async def on_disconnect(self):
        print("Bot apagado")
    

    @Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} ha entrado al servidor")


    @Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} ha salido del servidor")
    

    @Cog.listener()
    async def on_member_join(self, member):
        # Obtener el canal de bienvenida del servidor
        welcome_channel = member.guild.system_channel()
        if welcome_channel is not None:
            # Enviar mensaje de bienvenida
            await welcome_channel.send(f'Bienvenido {member.mention} al servidor!')

    @Cog.listener()
    async def on_ready(self):
        print('eventos.py online.')


async def setup(bot:Bot):
    print('I am being loaded from eventos.py')    
    await bot.add_cog(MyEvents(bot))


async def teardown(bot:Bot):
    print('Ha sido descargado eventos.py!')
    await bot.remove_cog(MyEvents(bot))
    
