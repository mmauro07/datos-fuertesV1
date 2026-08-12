from dataclasses import dataclass
from datetime import date

@dataclass
class LiquidacionSueldos:
    legajo: int
    fecha: date
    monto: float