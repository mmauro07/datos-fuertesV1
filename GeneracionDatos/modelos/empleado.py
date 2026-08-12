from dataclasses import dataclass
from datetime import date

from modelos.persona import Persona


@dataclass
class Empleado:
    legajo: int
    persona: Persona
    fechaIngreso: date
    idCargo: int
    idTurno: int