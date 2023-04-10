import aioodbc
import os

from abc import ABCMeta, abstractmethod
from dotenv import load_dotenv

load_dotenv()


server = os.getenv('SERVER')
database = os.getenv('DATABASE')


class Database(metaclass=ABCMeta):
    """Clase abstracta para obtener conexion y que cada clase hija realice query de la base de datos.
    \nMetodo abstracto: \n
        query(): Disponible para implementar funcion que uno desee conectando a la base de datos"""
    def __init__(self) -> None:
        self.dsn = 'DRIVER={SQL Server};SERVER=' + server + \
                ';DATABASE='+database + ';Trusted_Connection=yes;'


    async def connection_sqlserver(self):
        try:
            connection = await aioodbc.connect(dsn=self.dsn)
            return connection

        except TimeoutError:
            return f'No fue posible conectarse a la base de datos SQL Server, tiempo excedido'


    @abstractmethod
    async def query(self):
        pass




