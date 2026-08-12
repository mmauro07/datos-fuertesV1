from dataclasses import dataclass
from datetime import date


@dataclass
class Persona:
    dni: int
    nombre: str
    apellido: str
    fechaNacimiento: date
    telefono: str
    correoElectronico: str

    direccionDomicilio: str
    numeroDomicilio: int
    pisoDomicilio: int | None
    codigoPostalDomicilio: int