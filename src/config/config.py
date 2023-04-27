import os
from dotenv import load_dotenv


load_dotenv()


DATOS_DATABASE = {
    'server':os.getenv('SERVER'),
    'database': os.getenv('DATABASE'),
    'driver':'{SQL Server}',
}


SERVER = DATOS_DATABASE['server']
DATABASE = DATOS_DATABASE['database']
DRIVER = DATOS_DATABASE['driver']
TOKEN = os.getenv('BOT_SECRET_TOKEN')


DSN = {
    'dsn': f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
}

