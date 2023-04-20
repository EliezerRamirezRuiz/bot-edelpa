import discord
from Database.db import Conexion



class Stock(Conexion):
    async def get_data(self, code) :
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una Stock. En caso de que el resultado que 
        traiga es igual a None, mandara un mensaje de 'codigo invalido'
        """

        try:
            conn = await self.connection_sqlserver()
            async with conn.cursor() as cursor:
                query = f" EXEC  ObtenerStock {code} "
                await cursor.execute(query)
                row = await cursor.fetchone()

        except TimeoutError:
            return []

        else:  
            if row is None:
                return []
                
            return row
        
        finally:
            await cursor.close()
            await conn.close()
        

    async def return_stock(self, code: str):
        """ Funcion que usa `self.get_data` para obtener datos """
        stock = await self.get_data(code)

        if len(stock) > 0:
            embed = discord.Embed(title='Stock Material')
            embed.add_field(name=f'Material: {stock[0]}'
                        ,value=f'Cantidad: {stock[1]}')
            
            return embed
        
        else:
            embed = discord.Embed(title='Stock Material')
            embed.add_field(name=f'Material: No Encontrado'
                        ,value=f'Cantidad: Null')
            
            return embed

