from dataclasses import dataclass
from datetime import datetime


@dataclass
class FichadaSocio:
    dni: str
    fechaHora: datetime