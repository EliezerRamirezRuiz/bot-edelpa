from discord.ext import commands

class MyEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'{message.author.name} sent a message: {message.content}')
    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found.')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing required argument.')

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('This command has been disabled.')

        else:
            print(error)  # Print the error to the console
            await ctx.send('An error occurred while executing the command.')



    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f"Command '{ctx.command.name}' was used by {ctx.author.name} # {ctx.author.discriminator}")


    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(f"Command '{ctx.command}' was successfully executed")


    @commands.Cog.listener()
    async def on_connect(self):
        print("Bot Working")

    
    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Bot off")
    

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} ha entrado al servidor")


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} ha salido del servidor")
    

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Obtener el canal de bienvenida del servidor
        welcome_channel = member.guild.system_channel()
        if welcome_channel is not None:
            # Enviar mensaje de bienvenida
            await welcome_channel.send(f'Bienvenido {member.mention} al servidor!')