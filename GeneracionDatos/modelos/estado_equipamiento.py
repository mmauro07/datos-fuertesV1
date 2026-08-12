from dataclasses import dataclass
from datetime import datetime

@dataclass
class EstadoEquipamiento:
    codigoEquipamiento: int
    fechaHoraCambio: datetime
    idEstadoEquipamiento: int