from config import EJERCICIOS
from modelos.ejercicio import Ejercicio

class GeneradorEjercicio:

    def generar(self):

        ejercicios = []

        for codigo, datos in enumerate(EJERCICIOS, start=1):

            ejercicios.append(
                Ejercicio(
                    codigoEjercicio=codigo,
                    nombre=datos[0],
                    descripcion=datos[1],
                    idGrupoMuscular=datos[2],
                    idDificultad=datos[3],
                    idTipoEjercicio=datos[4]
                )
            )

        return ejercicios