import aioodbc
import os

from abc import ABCMeta, abstractmethod
from dotenv import load_dotenv


load_dotenv()


class Conexion(metaclass=ABCMeta):
    """Clase abstracta que retorna una conexion """
    

    def __init__(self) -> None:
        self.server = os.getenv('SERVER')
        self.database = os.getenv('DATABASE')
        self.dsn = 'DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE='+ self.database + ';Trusted_Connection=yes;'


    async def connection_sqlserver(self):
        try:
            connection = await aioodbc.connect(dsn=self.dsn)
            return connection

        except TimeoutError:
            return f'No fue posible conectarse a la base de datos SQL Server, tiempo excedido'


    @abstractmethod
    async def get_data(self):
        ...



