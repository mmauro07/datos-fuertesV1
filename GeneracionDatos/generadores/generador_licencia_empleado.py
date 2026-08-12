import random
from datetime import timedelta

from config import MOTIVOS_LICENCIA
from modelos.licencia_empleado import LicenciaEmpleado


class GeneradorLicenciasEmpleado:

    def generar(self, estados_empleado):

        licencias = []

        for estado in estados_empleado:

            # Solo los empleados en licencia
            if estado.idEstadoEmp != 2:
                continue

            fecha_fin = estado.fecha + timedelta(
                days=random.randint(7, 90)
            )

            motivo = random.choice(MOTIVOS_LICENCIA)

            licencias.append(
                LicenciaEmpleado(
                    legajo=estado.legajo,
                    fecha=estado.fecha,
                    fechaFinLicencia=fecha_fin,
                    motivo=motivo
                )
            )

        return licencias