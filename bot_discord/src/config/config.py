from discord import SelectOption
from dotenv import load_dotenv
import os

load_dotenv()

SERVER = str(os.environ.get('SERVER', '10.0.0.80'))
DATABASE = str(os.environ.get('DATABASE', 'BotDB'))
DRIVER = str(os.environ.get('SQL_SERVER', '{SQL SERVER}'))
UID = str(os.environ.get('UID', 'sap'))
PWD = str(os.environ.get('PWD','SAPedelpa2014'))
TOKEN = str(os.environ.get('BOT_SECRET_TOKEN','MTEwOTEyNDA1NzkyMTc1MzIxOQ.G7vhUg.AYiI3Quq25cyBg-3Jbfxl5mwtJx3H3Tg5C7eXE'))

DSN = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={UID};PWD={PWD}'

VALUES = [
        SelectOption(label="Default", default=True, value="Default", description="default"),
        SelectOption(label="Consultar Stock", value="Consultar Stock", description="Consultar stock de producto X"),
        SelectOption(label="Estado Robot", value="Estado Robot", description="Saber el estado actual del robot - [Trabajando - Parado]"),
        SelectOption(label="Ultimas alertas activas", value="Ultimas alertas activas", description="Saber la informacion de las alertas desactivadas (TOP 10)"),
        SelectOption(label="Ultimas alertas desactivadas", value="Ultimas alertas desactivadas", description="Saber la informacion de las alertas desactivadas (TOP 10)"),
]




