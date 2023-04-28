"""Archivo para manipular las acciones de """
from src.database.db import conexion_db, comprobar_largo, create_embed
from discord import Embed


class Stock():
    async def obtener_stock(self, code:str, ctx) -> list :
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una Stock. En caso de que el resultado que 
        traiga es igual a None, se mandara lista vacia'
        """

        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC  ObtenerStock {code} "
                    await cursor.execute(query)
                    row = await cursor.fetchone()
                    if row is None:
                        return []
                
                    return row

        except Exception as ex:
            """Casos de error durante ejecucion"""
            if isinstance(ex, TimeoutError):
                await ctx.send('Tiempo de espera excedido, reintente')
                
            else:
                await ctx.send('Error, porfavor contactar con el administrador del Bot')

        
    async def return_stock(self, code:str, ctx) -> Embed :
        """ Funcion para retornar los datos de `obtener_stock` """
        stock = await self.obtener_stock(code, ctx)

        if comprobar_largo(stock) is True:
            embed = create_embed(title="Stock del material", description="""consulta de material""",
                                fields=[{'name':'Material', 'value':f'{stock[0]}', 'inline':False},
                                {'name':'Cantidad', 'value':f'{stock[1]}', 'inline':False}])
            return embed
        
        else:
            embed = create_embed(title="Material no encontrado", description="""consulta de material""",
                                fields=[{'name':'Material', 'value':'None', 'inline':False},
                                {'name':'Cantidad', 'value':'None', 'inline':False}])
            
            return embed

