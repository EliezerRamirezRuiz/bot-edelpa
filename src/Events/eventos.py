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
            await ctx.send('Command not found. know more with !help')

        elif isinstance(error, MissingRequiredArgument):
            await ctx.send('Missing required argument.')

        elif isinstance(error, DisabledCommand):
            await ctx.send('This command has been disabled.')

        else:
            print(error)  # Print the error to the console
            await ctx.send('An error occurred while executing the command.')


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


async def setup(bot:Bot):
    print('I am being loaded from eventos.py')    
    await bot.add_cog(MyEvents(bot))


    
