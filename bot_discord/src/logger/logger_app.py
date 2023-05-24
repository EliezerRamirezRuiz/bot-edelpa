from logging import getLogger
from logging import Formatter
from logging.handlers import RotatingFileHandler
from logging import INFO
    
logger = getLogger()
logger.setLevel(INFO)
my_handler = RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=0,
)
my_handler.setLevel(INFO)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
my_handler.setFormatter(formatter)
logger.addHandler(my_handler)






