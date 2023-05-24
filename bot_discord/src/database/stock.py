from src.utils.funciones_utiles import comprobar_largo, create_embed
from src.database.conexion import conexion_db

from src.logger.logger_app import my_handler
from logging import makeLogRecord
from logging import INFO, WARNING

class StockBaseDeDatos:
    async def obtener_stock(self, code:str) -> list :
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC  OBTENERSTOCK '{code}' "
                    await cursor.execute(query)
                    row = await cursor.fetchone()

                    if row is None:
                        row = []
                        return  row
                    else:
                        return row

            
        except Exception as ex:
            my_handler.emit(makeLogRecord({'msg': f"error: {ex}", 'levelno': INFO, 'levelname':'INFO'}))


    async def return_stock(self, codigo:str):
        stock = await self.obtener_stock(codigo)
        print(stock)

        if comprobar_largo(stock) is True:
            embed = create_embed(title="Stock del material", description="""consulta de material""",
                                footer={'text':'Envases del Pacifico - Edelpa'}, 
                                fields=[{'name':'Material', 'value':f'{stock[0]}', 'inline':False},
                                        {'name':'Codigo', 'value':codigo, 'inline':False},
                                        {'name':'Cantidad', 'value':f'{stock[1]}', 'inline':False}])
            
            return embed

        else:
            embed = create_embed(title="Material no encontrado", description="""consulta de material""",
                                footer={'text':'Envases del Pacifico - Edelpa'}, 
                                fields=[{'name':'Material', 'value':'Null', 'inline':False},
                                        {'name':'Codigo', 'value':codigo, 'inline':False},
                                        {'name':'Cantidad', 'value':'Null', 'inline':False}])
            
            return embed

