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


#Ping-pong
@bot.command()
async def ping(ctx):
     await ctx.send('pong')


@bot.command
async def send_questionnaire(ctx,user):
    questions = [
        {
            "question": "What is your name?",
            "response": None
        },
        {
            "question": "What is your age?",
            "response": None
        }
    ]
    
    for question in questions:
        await user.send(question["question"])
        response = await bot.wait_for("message", check=lambda message: message.author == user)
        question["response"] = response.content
        await ctx.send('ahcv')
    # Do something with the responses, such as saving them to a database


@bot.event
async def on_guild_channel_create(channel):
    print(f"New channel created: {channel.name}")
    # Add code to do something with the new channel, like setting permissions or sending a welcome message

@bot.event
async def on_guild_channel_delete(channel):
    print(f"Channel deleted: {channel.name}")
    # Add code to do something when a channel is deleted, like removing it from a list of tracked channels

@bot.event
async def on_guild_role_create(role):
    print(f"New role created: {role.name}")
    # Add code to do something with the new role, like setting permissions or adding it to a list of roles

@bot.event
async def on_guild_role_delete(role):
    print(f"Role deleted: {role.name}")
    # Add code to do something when a role is deleted, like removing it from a list of tracked roles


@bot.event
async def on_command_error(ctx, error):
    """Function to return a error what we wanted"""
    print(f"What has happened: {ctx, error}")
    await ctx.send(f'error: "{error}"')
    # Add code to do something when a role is deleted, like removing it from a list of tracked roles





bot.run(token=Token)