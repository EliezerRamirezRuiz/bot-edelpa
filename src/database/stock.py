"""Archivo para manipular las acciones de """
from src.database.db import conexion_db
from discord import Embed
from src.utils.funciones_utiles import comprobar_largo, create_embed


class StockDB:
    async def obtener_stock(self, code:str) -> list :
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una Stock. En caso de que el resultado que 
        traiga es igual a None, se mandara lista vacia'
        """

        async with await conexion_db() as conn:
            async with conn.cursor() as cursor:
                query = f" EXEC  OBTENERSTOCK {code} "
                await cursor.execute(query)
                row = await cursor.fetchone()
                print(row)
                if row is None:
                    return []
                
                return row

        
    async def return_stock(self, code:str) -> Embed :
        """ Funcion para retornar los datos de `obtener_stock` """
        stock = await self.obtener_stock(code)
        print(stock)

        if comprobar_largo(stock) is True:
            embed = create_embed(title="Stock del material", description="""consulta de material""",
                                footer={'text':'Envases del Pacifico - Edelpa'}, 
                                fields=[{'name':'Material', 'value':f'{stock[0]}', 'inline':False},
                                {'name':'Cantidad', 'value':f'{stock[1]}', 'inline':False}])
            return embed
        
        else:
            embed = create_embed(title="Material no encontrado", description="""consulta de material""",
                                footer={'text':'Envases del Pacifico - Edelpa'}, 
                                fields=[{'name':'Material', 'value':'Null', 'inline':False},
                                        {'name':'Codigo', 'value':code, 'inline':False},
                                        {'name':'Cantidad', 'value':'Null', 'inline':False}])
            
            return embed

