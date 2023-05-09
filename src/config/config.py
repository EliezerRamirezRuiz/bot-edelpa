import os
from dotenv import load_dotenv


load_dotenv()


DATOS_DATABASE = {
    'server':str(os.environ.get('SERVER', '10.0.0.80')),
    'database': str(os.environ.get('DATABASE', 'BotDB')),
    'driver':str(os.environ.get('SQL_SERVER', '{SQL SERVER}')),
    'uid': str(os.environ.get('UID', 'sap')),
    'pwd':str(os.environ.get('PWD','SAPedelpa2014'))
}


SERVER = DATOS_DATABASE['server']
DATABASE = DATOS_DATABASE['database']
DRIVER = DATOS_DATABASE['driver']
UID = DATOS_DATABASE['uid']
PWD = DATOS_DATABASE['pwd']

TOKEN = os.getenv('BOT_SECRET_TOKEN')


DSN = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={UID};PWD={PWD}'



