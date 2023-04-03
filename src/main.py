"""library used - All are in requirements.txt"""
import os
import logging
import discord
import asyncio


from discord.ext import commands
from Functions import *
from dotenv import load_dotenv
from threading import Thread
from Functions.Complements.complements import test

load_dotenv()



"""Variables"""
token = os.environ["BOT_SECRET_TOKEN"]
descripcion = """Hola soy el bot de Edelpa S.A, \nte ayudare a enterarte de las alertas mas recientes del robot."""

""" Obligatory to retry connection"""
intents = discord.Intents.default()
intents.message_content = True

""" Instance Bot """
bot = commands.Bot(command_prefix='!', description=descripcion,
                   intents=intents, help_command=CustomHelpCommand())

"""Configuration Bot"""
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='r+')


@bot.event
async def on_ready():
    """Function when the Bot is ready to answer commands"""
    await bot.add_cog(MyEvents(bot))
    await bot.add_cog(MenuCommands(bot))
    await bot.add_cog(PrincipalCommands(bot))

    print(f"Hello user {bot.user}")


async def main():
    """Function to run the Bot"""
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(bot.start(token))

    except Exception as error:
        return f'error: {error}\nerror cause: {error.__cause__}'


if __name__ == '__main__':
    asyncio.run(main())
    
        
    
