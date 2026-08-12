from dataclasses import dataclass
from datetime import date

@dataclass
class EstadoEmpleado:
    legajo: int
    fecha: date
    idEstadoEmp: int