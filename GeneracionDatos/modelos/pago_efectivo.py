from dataclasses import dataclass
from datetime import date


@dataclass
class PagoEfectivo:
    dniSocio: str
    fechaInicio: date
    importeRecibido: float
    vuelto: float