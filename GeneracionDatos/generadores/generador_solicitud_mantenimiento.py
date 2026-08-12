import random
from datetime import timedelta

from modelos.solicitud_mantenimiento import SolicitudMantenimiento
from config import (
    FECHA_ACTUAL,
    PROBABILIDAD_SOLICITUD,
    DESCRIPCIONES_PROBLEMAS
)


class GeneradorSolicitudMantenimiento:

    def generar(
        self,
        equipamientos,
        empleados,
        estados_empleado
    ):

        solicitudes = []

        empleados_activos = self._obtener_empleados_activos(
            empleados,
            estados_empleado
        )

        entrenadores = [
            e for e in empleados_activos
            if e.idCargo == 1
        ]

        recepcionistas = [
            e for e in empleados_activos
            if e.idCargo == 2
        ]

        for equipamiento in equipamientos:

            fechas_utilizadas = set()

            probabilidad = PROBABILIDAD_SOLICITUD[
                equipamiento.idTipoEquipamiento
            ]

            cantidad = random.choices(
                [0, 1, 2],
                weights=[
                    1 - probabilidad,
                    probabilidad * 0.85,
                    probabilidad * 0.15
                ],
                k=1
            )[0]

            fecha_minima = equipamiento.fechaAdquisicion

            for _ in range(cantidad):

                while True:

                    fecha = self._generar_fecha(
                        fecha_minima,
                        FECHA_ACTUAL
                    )

                    if fecha not in fechas_utilizadas:
                        fechas_utilizadas.add(fecha)
                        break

                if entrenadores and random.random() < 0.9:
                    empleado = random.choice(entrenadores)
                else:
                    empleado = random.choice(recepcionistas)

                solicitudes.append(
                    SolicitudMantenimiento(
                        codigoEquipamiento=equipamiento.codigoEquipamiento,
                        fechaSolicitud=fecha,
                        legajo=empleado.legajo,
                        descripcionProblema=random.choice(
                            DESCRIPCIONES_PROBLEMAS
                        )
                    )
                )

                # Si habrá otra solicitud,
                # debe ser posterior a la anterior.
                fecha_minima = fecha + timedelta(days=1)

                if fecha_minima > FECHA_ACTUAL:
                    break

        return solicitudes

    def _obtener_empleados_activos(
        self,
        empleados,
        estados_empleado
    ):

        ultimos_estados = {}

        for estado in sorted(
            estados_empleado,
            key=lambda e: e.fecha
        ):
            ultimos_estados[estado.legajo] = estado.idEstadoEmp

        return [
            empleado
            for empleado in empleados
            if ultimos_estados.get(empleado.legajo) == 1
        ]

    def _generar_fecha(
        self,
        fecha_inicio,
        fecha_fin
    ):

        dias = (fecha_fin - fecha_inicio).days

        return fecha_inicio + timedelta(
            days=random.randint(0, dias)
        )