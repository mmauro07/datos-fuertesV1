from dataclasses import dataclass
from datetime import date

@dataclass
class MantenimientoHecho:
    codigoEquipamiento: int
    fechaSolicitud: date
    fechaReincorporacion: date
    costoReparacion: float | None