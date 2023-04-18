from Database.Clases.alerta import Alerta
from Database.Clases.automic import AutomaticAlerta
from Database.Clases.reporte import Reporte
from Database.Clases.robot import Robot
from Database.Clases.stock import Stock


alerta = Alerta()
robot =  Robot()
stock = Stock()
report = Reporte()
alerta_automatica = AutomaticAlerta()



__all__ = [
            'alerta'
            ,'robot'
            ,'stock'
            ,'report'
            ,'alerta_automatica'
                                ]