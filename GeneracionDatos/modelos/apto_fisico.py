from dataclasses import dataclass
from datetime import date


@dataclass
class AptoFisico:

    dniSocio: int
    fechaPresentacion: date
    fechaVencimiento: date