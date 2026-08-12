from dataclasses import dataclass
from datetime import date

from modelos.persona import Persona


@dataclass
class Socio:
    persona: Persona
    fechaAlta: date