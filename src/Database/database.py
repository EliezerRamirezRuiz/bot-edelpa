import aioodbc
import os
import datetime

from aioodbc.connection import _ContextManager
from abc import ABCMeta, abstractmethod
from dotenv import load_dotenv


load_dotenv()


NOW = datetime.datetime.now()

class Conexion(metaclass=ABCMeta):
    """Clase abstracta que retorna una conexion """
    

    def __init__(self) -> None:
        self.server = os.getenv('SERVER')
        self.database = os.getenv('DATABASE')
        self.dsn = 'DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE='+ self.database + ';Trusted_Connection=yes;'


    async def connection_sqlserver(self) -> _ContextManager:
        
        try:
            connection = await aioodbc.connect(dsn=self.dsn)
            return connection

        except Exception:
            return f'''Fue imposible obtener una respuesta del servidor,
                porfavor contacte con el administrador de Area Informatica'''


    @abstractmethod
    async def get_data(self):
        pass



