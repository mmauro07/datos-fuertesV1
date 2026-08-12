import random
from datetime import datetime, timedelta, time

from config import (
    FECHA_ACTUAL,
    HORARIOS_TURNO,
    PROBABILIDAD_ASISTENCIA
)
from modelos.fichada_empleado import FichadaEmpleado


class GeneradorFichadasEmpleado:

    def generar(self, empleados, estados_empleado):

        fichadas = []

        fechas_fin = self._obtener_fechas_fin_actividad(estados_empleado)

        for empleado in empleados:

            # Solo empleados activos
            fecha = empleado.fechaIngreso
            fecha_fin = fechas_fin[empleado.legajo]

            while fecha <= fecha_fin:

                # El empleado no asistió ese día
                if random.random() > PROBABILIDAD_ASISTENCIA:
                    fecha += timedelta(days=1)
                    continue

                horario = HORARIOS_TURNO[empleado.idTurno]

                hora_entrada = self._generar_hora(*horario["entrada"])
                hora_salida = self._generar_hora(*horario["salida"])

                fecha_hora_entrada = datetime.combine(
                    fecha,
                    hora_entrada
                )

                fecha_salida = fecha

                # Si trabaja de noche sale al día siguiente
                if empleado.idTurno == 3:
                    fecha_salida += timedelta(days=1)

                fecha_hora_salida = datetime.combine(
                    fecha_salida,
                    hora_salida
                )

                fichadas.append(
                    FichadaEmpleado(
                        legajo=empleado.legajo,
                        fechaHora=fecha_hora_entrada,
                        idTipoMovimiento=1
                    )
                )

                fichadas.append(
                    FichadaEmpleado(
                        legajo=empleado.legajo,
                        fechaHora=fecha_hora_salida,
                        idTipoMovimiento=2
                    )
                )

                fecha += timedelta(days=1)

        return fichadas

    def _obtener_fechas_fin_actividad(self, estados_empleado):

        fechas_fin = {}

        for estado in sorted(estados_empleado, key=lambda e: e.fecha):

            # Si nunca cambia de estado, permanece activo
            if estado.legajo not in fechas_fin:
                fechas_fin[estado.legajo] = FECHA_ACTUAL

            # Si entra en licencia o renuncia, deja de fichar
            if estado.idEstadoEmp in (2, 3):
                fechas_fin[estado.legajo] = estado.fecha - timedelta(days=1)

        return fechas_fin

    def _generar_hora(self, hora_inicio, minuto_inicio,
                       hora_fin, minuto_fin):

        inicio = hora_inicio * 60 + minuto_inicio
        fin = hora_fin * 60 + minuto_fin

        minutos = random.randint(inicio, fin)

        return time(
            hour=minutos // 60,
            minute=minutos % 60
        )