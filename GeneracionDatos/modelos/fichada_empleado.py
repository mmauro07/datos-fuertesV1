from dataclasses import dataclass
from datetime import datetime

@dataclass
class FichadaEmpleado:
    legajo: int
    fechaHora: datetime
    idTipoMovimiento: int