from dataclasses import dataclass
from datetime import date

@dataclass
class Rutina:
    dniCliente: int
    fechaCreacion: date
    legajo: int
    idObjetivo: int
    observaciones: str | None