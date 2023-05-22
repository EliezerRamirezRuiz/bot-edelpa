from logging import getLogger
from logging import Formatter, StreamHandler
from logging import INFO
    
logger = getLogger()
logger.setLevel(INFO)

my_handler = StreamHandler()
my_handler.setLevel(INFO)

formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
my_handler.setFormatter(formatter)
logger.addHandler(my_handler)





