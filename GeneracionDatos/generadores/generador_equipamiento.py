import random
from config import CANTIDAD_EQUIPAMIENTO, MODELOS, DISTRIBUCION_ADQUISICION_EQUIPAMIENTO, FECHA_ACTUAL
from datetime import date, timedelta
from modelos.equipamiento import Equipamiento

class GeneradorEquipamiento:

    def generar(self):

        equipamientos = []

        codigo = 1

        for id_tipo, cantidad in CANTIDAD_EQUIPAMIENTO.items():

            for _ in range(cantidad):

                equipamientos.append(
                    Equipamiento(
                        codigoEquipamiento=codigo,
                        idTipoEquipamiento=id_tipo,
                        idModelo=random.choice(MODELOS),
                        fechaAdquisicion=self._generar_fecha_adquisicion()
                    )
                )

                codigo += 1

        return equipamientos

    def _generar_fecha_adquisicion(self):

        periodo = random.choices(
            population=list(DISTRIBUCION_ADQUISICION_EQUIPAMIENTO.keys()),
            weights=list(DISTRIBUCION_ADQUISICION_EQUIPAMIENTO.values()),
            k=1
        )[0]

        if periodo == "antes_apertura":
            return self._generar_fecha(
                date(2025, 1, 1),
                date(2025, 10, 5)
            )

        elif periodo == "fin_2025":
            return self._generar_fecha(
                date(2025, 10, 6),
                date(2025, 12, 31)
            )

        elif periodo == "primer_trimestre_2026":
            return self._generar_fecha(
                date(2026, 1, 1),
                date(2026, 3, 31)
            )

        return self._generar_fecha(
            date(2026, 4, 1),
            FECHA_ACTUAL
        )

    def _generar_fecha(self, fecha_inicio, fecha_fin):

        dias = (fecha_fin - fecha_inicio).days

        return fecha_inicio + timedelta(
            days=random.randint(0, dias)
        )