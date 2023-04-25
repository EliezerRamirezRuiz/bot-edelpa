"""Archivo para manipular las acciones de """
import discord
from Database.database import Conexion
from discord import Embed


class Stock(Conexion):
    async def get_data(self, code:str, ctx) -> list :
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una Stock. En caso de que el resultado que 
        traiga es igual a None, se mandara lista vacia'
        """

        try:
            conn = await self.connection_sqlserver()
            async with conn.cursor() as cursor:
                query = f" EXEC  ObtenerStock {code} "
                await cursor.execute(query)
                row = await cursor.fetchone()

        except Exception:
            """Caso de error durante ejecucion"""
            return ctx.send('No se pudo obtener el stock, contacte con el encargado de informatica')

        else: 
            print(row)
            if row is None:
                return []
                
            return row
        
        finally:
            await cursor.close()
            await conn.close()
        

    async def return_stock(self, code: str) -> Embed :
        """ Funcion para retornar los datos de `get_data` """
        stock = await self.get_data(code)

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

