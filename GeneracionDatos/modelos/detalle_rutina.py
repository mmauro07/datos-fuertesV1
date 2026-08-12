from dataclasses import dataclass
from datetime import date

@dataclass
class DetalleRutina:
    dniCliente: int
    fechaCreacion: date
    orden: int
    codigoEjercicio: int
    cantidadSeries: int
    cantidadRepeticiones: int
    descansoSegundos: int
    observaciones: str | None