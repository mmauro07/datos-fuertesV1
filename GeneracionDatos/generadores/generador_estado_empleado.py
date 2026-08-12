from datetime import date, timedelta
import random

from config import DISTRIBUCION_ESTADOS_EMPLEADO
from modelos.estado_empleado import EstadoEmpleado

class GeneradorEstadosEmpleado:

    def generar(self, empleados):

        estados = []

        for empleado in empleados:

            estados.append(
                            EstadoEmpleado(
                                legajo=empleado.legajo,
                                fecha=empleado.fechaIngreso,
                                idEstadoEmp=1
                                )
                            )

            id_estado = random.choices(
                population=list(DISTRIBUCION_ESTADOS_EMPLEADO.keys()),
                weights=list(DISTRIBUCION_ESTADOS_EMPLEADO.values()),
                k=1
            )[0]

            if id_estado == 1:
                continue

            else:
                estados.append(
                    EstadoEmpleado(
                        legajo=empleado.legajo,
                        fecha=self._generar_fecha_cambio(
                            empleado.fechaIngreso
                        ),
                        idEstadoEmp=id_estado
                    )
                )

        return estados

    def _generar_fecha_cambio(self, fecha_ingreso):

        dias = (date.today() - fecha_ingreso).days

        return fecha_ingreso + timedelta(
            days=random.randint(1, dias)
        )