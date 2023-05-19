"""Archivo para manipular las acciones de """
from src.utils.funciones_utiles import comprobar_largo, create_embed
from src.database.conexion_basededatos import conexion_db
from src.database.procedimientos import ProcedimientosAlmacenados


class StockBaseDeDatos:
    def __init__(self) -> None:
        self.procedimiento = ProcedimientosAlmacenados()


    async def obtener_stock(self, code:str) -> list :
        """Funcion que trae el stock que sera implementada por la clase Stock"""
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC  OBTENERSTOCK {code} "
                    await cursor.execute(query)
                    row = await cursor.fetchone()

                    if row is None:
                        row = []
                        return  row
                    else:
                        return row

            
        except Exception as ex:
                print(f'error: {ex}')


    async def return_stock(self, codigo:str):
        """ Funcion para retornar los datos de `obtener_stock` """
        stock = await self.procedimiento.obtener_stock(codigo)
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

