import random

from modelos.recepcionista import Recepcionista


class GeneradorRecepcionistas:

    def generar(self, empleados, estados_empleado):

        recepcionistas = []

        ultimos_estados = self._obtener_ultimos_estados(estados_empleado)

        # Genera solo los recepcionistas activos
        for empleado in empleados:

            if empleado.idCargo != 2:
                continue

            if ultimos_estados.get(empleado.legajo) != 1:
                continue

            recepcionistas.append(
                Recepcionista(
                    legajo=empleado.legajo,
                    telCorpAsig=self._generar_telefono_corporativo()
                )
            )

        return recepcionistas

    def _obtener_ultimos_estados(self, estados_empleado):

        ultimos_estados = {}

        for estado in sorted(estados_empleado, key=lambda e: e.fecha):
            ultimos_estados[estado.legajo] = estado.idEstadoEmp

        return ultimos_estados

    def _generar_telefono_corporativo(self):

        return "11" + "".join(
            str(random.randint(0, 9))
            for _ in range(8)
        )