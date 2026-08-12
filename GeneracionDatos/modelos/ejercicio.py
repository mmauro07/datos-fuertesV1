from dataclasses import dataclass

@dataclass
class Ejercicio:
    codigoEjercicio: int
    nombre: str
    descripcion: str
    idGrupoMuscular: int
    idDificultad: int
    idTipoEjercicio: int