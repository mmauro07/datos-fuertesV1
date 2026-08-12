import random
from datetime import datetime, time, timedelta

from modelos.estado_equipamiento import EstadoEquipamiento
from config import PROBABILIDAD_FUERA_SERVICIO


class GeneradorEstadoEquipamiento:

    def generar(
        self,
        equipamientos,
        solicitudes,
        mantenimientos
    ):

        estados = []

        mantenimientos_dict = {
            (m.codigoEquipamiento, m.fechaSolicitud): m
            for m in mantenimientos
        }

        solicitudes_por_equipo = {}

        for solicitud in solicitudes:
            solicitudes_por_equipo.setdefault(
                solicitud.codigoEquipamiento,
                []
            ).append(solicitud)

        for lista in solicitudes_por_equipo.values():
            lista.sort(key=lambda s: s.fechaSolicitud)

        for equipamiento in equipamientos:

            # Fechas ya utilizadas para ESTE equipamiento
            fechas_utilizadas = set()

            # Estado inicial
            fecha = self._obtener_fecha_unica(
                equipamiento.fechaAdquisicion,
                time(8, 0),
                fechas_utilizadas
            )

            estados.append(
                EstadoEquipamiento(
                    codigoEquipamiento=equipamiento.codigoEquipamiento,
                    fechaHoraCambio=fecha,
                    idEstadoEquipamiento=1
                )
            )

            for solicitud in solicitudes_por_equipo.get(
                equipamiento.codigoEquipamiento,
                []
            ):

                # Pasa a mantenimiento
                fecha = self._obtener_fecha_unica(
                    solicitud.fechaSolicitud,
                    time(9, 0),
                    fechas_utilizadas
                )

                estados.append(
                    EstadoEquipamiento(
                        codigoEquipamiento=equipamiento.codigoEquipamiento,
                        fechaHoraCambio=fecha,
                        idEstadoEquipamiento=2
                    )
                )

                mantenimiento = mantenimientos_dict.get(
                    (
                        solicitud.codigoEquipamiento,
                        solicitud.fechaSolicitud
                    )
                )

                if mantenimiento:

                    id_estado = (
                        3
                        if random.random() < PROBABILIDAD_FUERA_SERVICIO
                        else 1
                    )

                    fecha = self._obtener_fecha_unica(
                        mantenimiento.fechaReincorporacion,
                        time(17, 0),
                        fechas_utilizadas
                    )

                    estados.append(
                        EstadoEquipamiento(
                            codigoEquipamiento=equipamiento.codigoEquipamiento,
                            fechaHoraCambio=fecha,
                            idEstadoEquipamiento=id_estado
                        )
                    )

        return estados

    def _obtener_fecha_unica(
        self,
        fecha,
        hora,
        fechas_utilizadas
    ):

        fecha_hora = datetime.combine(fecha, hora)

        while fecha_hora in fechas_utilizadas:
            fecha_hora += timedelta(seconds=1)

        fechas_utilizadas.add(fecha_hora)

        return fecha_hora