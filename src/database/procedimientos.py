from src.database.conexion_basededatos import conexion_db


class ProcedimientosAlmacenados():
    async def obtener_alertas(self) -> list:
        """ Funcion para traer datos `{Procedure MANDAR_ALERTAS}` """
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f"EXEC MANDAR_ALERTAS"
                    await cursor.execute(query)
                    row = await cursor.fetchall()

                    if not row:
                        return []
    
                    return row
                
        except Exception as ex:
            if isinstance(ex, TimeoutError):
                print('Tiempo excedido')

            else:
                print(f'error: {ex}')


    async def cambiar_estado_alerta(self, id:int) -> None:
        """Funcion que executa un procedimiento almacenado que apaga las alarmas,
        se ejecutará despues de que no haya intentos a realizar `self.auto_alertas()`"""
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC APAGAR_ALERTAS {id}"
                    await cursor.execute(query)

        except Exception as ex:
            if isinstance(ex, TimeoutError):
                print('Tiempo excedido')
            else:
                print(f'error: {ex}')


    async def bajar_contador_alertas(self, id: int) -> None:
        """Funcion para bajar el contador de veces que se debe executar una alerta"""
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC BAJAR_CONTADOR_ALERTA {id}"
                    await cursor.execute(query)

        except Exception as ex:
            if isinstance(ex, TimeoutError):
                print('Tiempo excedido')
            else:
                print('Error durante la ejecución del procedimiento almacenado')

        
    async def obtener_stock(self, code:str) -> list :
        """ Funcion para traer datos de la base de datos SQL Server, 
        para ser mas exacto una Stock. En caso de que el resultado que 
        traiga es igual a None, se mandara lista vacia'
        """

        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC  OBTENERSTOCK {code} "
                    await cursor.execute(query)
                    row = await cursor.fetchone()
                    print(row)
                    if row is None:
                        return []
                
                    return row
            
        except Exception as ex:
            if isinstance(ex, TimeoutError):
                print('Tiempo excedido')
                
            else:
                print('Error durante la ejecución del procedimiento almacenado')


    async def alertas_activas(self) -> list:
        """ Funcion que trae las ultimas alertas activas """
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC ULTIMAS_ALERTAS_ACTIVAS "
                    await cursor.execute(query)
                    row = await cursor.fetchall()
                    if row is None:
                        return []
                
                    return row 

        except Exception as ex:
            if isinstance(ex, TimeoutError):
                print('Tiempo excedido')
            
            else:
                print('Error desconocido')


    async def alertas_desactivadas(self):
        """ Funcion que trae las ultimas alertas inactivas """
        try:
            async with await conexion_db() as conn:
                async with conn.cursor() as cursor:
                    query = f" EXEC ULTIMAS_ALERTAS_DESACTIVADAS "
                    await cursor.execute(query)
                    row = await cursor.fetchall()
                    if row is None:
                        return []
                
                    return row 
                
        except Exception as ex:
            if isinstance(ex, TimeoutError):
                print('Tiempo excedido')
        
            else:
                print('Error desconocido')