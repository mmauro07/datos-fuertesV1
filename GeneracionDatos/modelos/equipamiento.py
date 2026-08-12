from dataclasses import dataclass
from datetime import date

@dataclass
class Equipamiento:
    codigoEquipamiento: int
    idTipoEquipamiento: int
    idModelo: int
    fechaAdquisicion: date