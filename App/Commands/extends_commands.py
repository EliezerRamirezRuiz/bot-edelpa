from discord.ext import commands

class MyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def my_command(self, ctx):
        await ctx.send('Hello from MyCommand!')
