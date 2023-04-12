from Funciones.Database.db import Database


class Stock(Database):
    async def get_data(self, code: str) :
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

                if row is None:
                    return 'codigo invalido'

                return row

        except TimeoutError as ex:
            return f'ocurrio: {ex.__cause__}'

        finally:
            await cursor.close()
            await conn.close()