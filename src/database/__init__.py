from src.database.automico import AlertaAutomatica
from src.database.reporte import ReporteDB
from src.database.alerta import AlertaDB
from src.database.robot import RobotDB
from src.database.stock import StockDB


instancia_alerta, instancia_robot, instancia_stock = AlertaDB(), RobotDB(), StockDB()
instancia_report, instancia_automatica =  ReporteDB(), AlertaAutomatica()


__all__ = [
            'instancia_alerta', 'instancia_robot', 'instancia_stock',
            'instancia_report', 'instancia_automatica'
        ]