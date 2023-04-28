from src.database.automico import AutomaticAlerta
from src.database.reporte import Reporte
from src.database.alerta import Alerta
from src.database.robot import Robot
from src.database.stock import Stock


instancia_alerta, instancia_robot, instancia_stock = Alerta(), Robot(), Stock()
instancia_report, instancia_automatica =  Reporte(), AutomaticAlerta()


__all__ = [
            'instancia_alerta', 'instancia_robot', 'instancia_stock',
            'instancia_report', 'instancia_automatica'
        ]