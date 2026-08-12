import calendar

from modelos.liquidacion_sueldos import LiquidacionSueldos
from config import (
    FECHA_ACTUAL,
    SUELDOS_BASE,
    ADICIONAL_TURNO,
    ADICIONAL_ANTIGUEDAD
)


class GeneradorLiquidacionesSueldos:

    def generar(self, empleados, estados_empleado):

        liquidaciones = []

        fecha_fin = self._obtener_fechas_fin_liquidacion(estados_empleado)

        for empleado in empleados:

            fecha = empleado.fechaIngreso.replace(day=1)

            while fecha <= fecha_fin[empleado.legajo]:

                ultimo_dia = calendar.monthrange(
                    fecha.year,
                    fecha.month
                )[1]

                fecha_liquidacion = fecha.replace(day=ultimo_dia)

                # Si ingresó después del cierre de ese mes,
                # no corresponde liquidar.
                if fecha_liquidacion >= empleado.fechaIngreso:

                    liquidaciones.append(
                        LiquidacionSueldos(
                            legajo=empleado.legajo,
                            fecha=fecha_liquidacion,
                            monto=self._calcular_sueldo(
                                empleado,
                                fecha_liquidacion
                            )
                        )
                    )

                fecha = self._sumar_mes(fecha)

        return liquidaciones

    def _obtener_fechas_fin_liquidacion(self, estados_empleado):

        fechas_fin = {}

        for estado in sorted(estados_empleado, key=lambda e: e.fecha):

            if estado.legajo not in fechas_fin:
                fechas_fin[estado.legajo] = FECHA_ACTUAL

            # Solo deja de liquidar cuando renuncia
            if estado.idEstadoEmp == 3:
                fechas_fin[estado.legajo] = estado.fecha

        return fechas_fin

    def _calcular_sueldo(self, empleado, fecha_liquidacion):

        sueldo = SUELDOS_BASE[empleado.idCargo]

        sueldo *= (
            1 + ADICIONAL_TURNO[empleado.idTurno]
        )

        antiguedad = (
            (fecha_liquidacion - empleado.fechaIngreso).days
            // 365
        )

        sueldo *= (
            1 + antiguedad * ADICIONAL_ANTIGUEDAD
        )

        return round(sueldo, 2)

    def _sumar_mes(self, fecha):

        if fecha.month == 12:
            return fecha.replace(
                year=fecha.year + 1,
                month=1
            )

        return fecha.replace(
            month=fecha.month + 1
        )