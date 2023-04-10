from Functions.Database.conexion_db import Database


class ObtenerStock(Database):
    async def query(self, code: str):
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una Stock """
        try:
            conn = await self.connection_sqlserver()
            async with conn.cursor() as cursor:
                query = f" EXEC  ObtenerStock {code} "
                await cursor.execute(query)
                row = await cursor.fetchone()

                if row is None:
                    return 'codigo invalido'

                return row

        except Exception as ex:
            return f'obtener stock no puede:{ex}'

        finally:
            await cursor.close()
            await conn.close()