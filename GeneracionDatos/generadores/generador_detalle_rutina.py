import random

from config import OBSERVACIONES_DETALLE_RUTINA
from modelos.detalle_rutina import DetalleRutina


class GeneradorDetalleRutina:

    def generar(self, rutinas, ejercicios):

        detalles = []

        for rutina in rutinas:

            cantidad_ejercicios = random.randint(6, 10)

            ejercicios_rutina = random.sample(
                ejercicios,
                cantidad_ejercicios
            )

            for orden, ejercicio in enumerate(
                ejercicios_rutina,
                start=1
            ):

                detalles.append(
                    DetalleRutina(
                        dniCliente=rutina.dniCliente,
                        fechaCreacion=rutina.fechaCreacion,
                        orden=orden,
                        codigoEjercicio=ejercicio.codigoEjercicio,
                        cantidadSeries=random.randint(3, 5),
                        cantidadRepeticiones=random.randint(8, 15),
                        descansoSegundos=random.choice(
                            [30, 45, 60, 90, 120]
                        ),
                        observaciones=random.choice(
                            OBSERVACIONES_DETALLE_RUTINA
                        )
                    )
                )

        return detalles