import aioodbc
import os

from abc import ABCMeta, abstractmethod
from dotenv import load_dotenv

load_dotenv()


class Database(metaclass=ABCMeta):
    r"""Clase abstracta para obtener conexion y que cada clase hija realice query de la base de datos.
            Metodo abstracto: 

        query(): Disponible para implementar funcion que uno desee conectando a la base de datos"""
    

    def __init__(self) -> None:
        self.server = os.getenv('SERVER')
        self.database = os.getenv('DATABASE')
        self.dsn = 'DRIVER={SQL Server};SERVER=' + self.server + \
                ';DATABASE='+ self.database + ';Trusted_Connection=yes;'


    async def connection_sqlserver(self):
        try:
            connection = await aioodbc.connect(dsn=self.dsn)
            return connection

        except TimeoutError:
            return f'No fue posible conectarse a la base de datos SQL Server, tiempo excedido'


    @abstractmethod
    async def get_data(self):
        ...



