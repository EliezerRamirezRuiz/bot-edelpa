from discord.ext import commands

class MyEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'{message.author.name} sent a message: {message.content}')
    

    @commands.Cog.listener()
    async def on_command_error(self, error):
        if isinstance(error, commands.CommandNotFound):
            await self.send('Command not found.')

        elif isinstance(error, commands.MissingRequiredArgument):
            await self.send('Missing required argument.')

        elif isinstance(error, commands.DisabledCommand):
            await self.send('This command has been disabled.')

        else:
            print(error)  # Print the error to the console
            await self.send('An error occurred while executing the command.')


    @commands.Cog.listener()
    async def on_command_error(self, error):
        if isinstance(error, commands.CommandNotFound):
            await self.send('Command not found.')

        elif isinstance(error, commands.MissingRequiredArgument):
          await self.send('Missing required argument.')

        elif isinstance(error, commands.DisabledCommand):
           await self.send('This command has been disabled.')
        else:
            print(error)  # Print the error to the console
            await self.send('An error occurred while executing the command.')


    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f"Command '{ctx.command.name}' was used by {ctx.author.name} # {ctx.author.discriminator}")


    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(f"Command '{ctx.command}' was successfully executed")
    

    
    