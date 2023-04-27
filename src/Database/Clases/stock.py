"""Archivo para manipular las acciones de """
from Database.database import conexion_db
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
                    
                    print(row)
                    if row is None:
                        return []
                
                    return row

        except Exception as ex:
            """Caso de error durante ejecucion"""
            if isinstance(ex, TimeoutError):
                await ctx.send('Tiempo de espera excedido, reintente')
                
            else:
                await ctx.send('Error, porfavor contactar con el administrador del Bot')

        
    async def return_stock(self, code:str) -> Embed :
        """ Funcion para retornar los datos de `obtener_stock` """
        stock = await self.obtener_stock(code)

        if len(stock) > 0:
            embed = Embed(title='Stock del Material')
            embed.set_author()
            embed.add_field(name=f'Material: {stock[0]}'
                        ,value=f'Cantidad: {stock[1]}')
            
            return embed
        
        else:
            embed = Embed(title='Stock Material')
            embed.add_field(name=f'Material: No Encontrado'
                        ,value=f'Cantidad: Null')
            
            return embed

