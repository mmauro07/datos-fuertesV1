from dataclasses import dataclass
from datetime import date

@dataclass
class LicenciaEmpleado:
    legajo: int
    fecha: date
    fechaFinLicencia: date
    motivo: str