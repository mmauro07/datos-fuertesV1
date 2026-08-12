from dataclasses import dataclass
from datetime import date

@dataclass
class SolicitudMantenimiento:
    codigoEquipamiento: int
    fechaSolicitud: date
    legajo: int
    descripcionProblema: str