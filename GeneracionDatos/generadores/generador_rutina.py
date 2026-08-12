import random
from datetime import timedelta

from config import (
    FECHA_ACTUAL,
    DISTRIBUCION_OBJETIVOS,
    PROBABILIDAD_NUEVA_RUTINA,
    OBSERVACIONES_RUTINA
)
from modelos.rutina import Rutina


class GeneradorRutinas:

    def generar(
        self,
        socios,
        empleados,
        estados_empleado,
        membresias
    ):

        rutinas = []

        entrenadores = self._obtener_entrenadores_activos(
            empleados,
            estados_empleado
        )

        membresias_por_socio = self._agrupar_membresias(
            membresias
        )

        for socio in socios:

            lista_membresias = miembros = membresias_por_socio.get(
                socio.persona.dni,
                []
            )

            claves_utilizadas = set()

            if not lista_membresias:
                continue

            for i, membresia in enumerate(lista_membresias):

                # La primera membresía siempre genera una rutina.
                # Las renovaciones solo algunas veces.
                if i > 0 and random.random() > PROBABILIDAD_NUEVA_RUTINA:
                    continue

                entrenador = random.choice(entrenadores)

                fecha_minima = max(
                    membresia.fechaInicio,
                    entrenador.fechaIngreso
                )

                if fecha_minima > FECHA_ACTUAL:
                    continue

                fecha_limite = min(
                                fecha_minima + timedelta(days=15),
                                FECHA_ACTUAL
                            )

                while True:

                    fecha_creacion = self._generar_fecha(
                        fecha_minima,
                        fecha_limite
                    )

                    clave = (socio.persona.dni, fecha_creacion)

                    if clave not in claves_utilizadas:
                        claves_utilizadas.add(clave)
                        break

                rutinas.append(
                    Rutina(
                        dniCliente=socio.persona.dni,
                        fechaCreacion=fecha_creacion,
                        legajo=entrenador.legajo,
                        idObjetivo=self._generar_objetivo(),
                        observaciones=random.choice(
                            OBSERVACIONES_RUTINA
                        )
                    )
                )

        return rutinas

    def _obtener_entrenadores_activos(
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
            if empleado.idCargo == 1
            and ultimos_estados.get(empleado.legajo) == 1
        ]

    def _agrupar_membresias(self, membresias):

        agrupadas = {}

        for membresia in membresias:

            agrupadas.setdefault(
                membresia.dniSocio,
                []
            ).append(membresia)

        for lista in agrupadas.values():
            lista.sort(key=lambda m: m.fechaInicio)

        return agrupadas

    def _generar_objetivo(self):

        return random.choices(
            population=list(DISTRIBUCION_OBJETIVOS.keys()),
            weights=list(DISTRIBUCION_OBJETIVOS.values()),
            k=1
        )[0]

    def _generar_fecha(
        self,
        fecha_inicio,
        fecha_fin
    ):

        dias = (fecha_fin - fecha_inicio).days

        return fecha_inicio + timedelta(
            days=random.randint(0, dias)
        )