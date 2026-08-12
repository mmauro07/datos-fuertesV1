from dataclasses import dataclass
from datetime import date

@dataclass
class Membresia:

    dniSocio: int
    fechaInicio: date
    fechaFin: date
    idTipoMembresia: int
    idMedioPago: int