from discord.ext import commands

class MyEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'{message.author.name} sent a message: {message.content}')
    
    

    
    