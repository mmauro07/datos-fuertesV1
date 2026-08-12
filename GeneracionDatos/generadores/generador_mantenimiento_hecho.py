import random
from datetime import timedelta

from modelos.mantenimiento_hecho import MantenimientoHecho
from config import (
    FECHA_ACTUAL,
    PROBABILIDAD_MANTENIMIENTO_REALIZADO,
    DIAS_REPARACION,
    COSTOS_REPARACION
)


class GeneradorMantenimientoHecho:

    def generar(self, solicitudes):

        mantenimientos = []

        for solicitud in solicitudes:

            if random.random() > PROBABILIDAD_MANTENIMIENTO_REALIZADO:
                continue

            fecha_reincorporacion = min(
                solicitud.fechaSolicitud +
                timedelta(
                    days=random.randint(
                        DIAS_REPARACION[0],
                        DIAS_REPARACION[1]
                    )
                ),
                FECHA_ACTUAL
            )

            costo = random.choices(
                population=[c[0] for c in COSTOS_REPARACION],
                weights=[c[1] for c in COSTOS_REPARACION],
                k=1
            )[0]

            mantenimientos.append(
                MantenimientoHecho(
                    codigoEquipamiento=solicitud.codigoEquipamiento,
                    fechaSolicitud=solicitud.fechaSolicitud,
                    fechaReincorporacion=fecha_reincorporacion,
                    costoReparacion=costo
                )
            )

        return mantenimientos