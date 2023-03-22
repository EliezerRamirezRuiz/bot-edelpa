from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

#cargamos las variables de entorno
load_dotenv()

#Captura las varibales de entorno en varibles
Token = os.environ["BOT_SECRET_TOKEN"]
Descripcion = """Hola soy el bot de Edelpa S.A, 
                te ayudare a enterarte de las alertas mas recientes del robot"""

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', description="Holaaaaaaaaaaaa", intents=intents)


bot.run(token=Token)