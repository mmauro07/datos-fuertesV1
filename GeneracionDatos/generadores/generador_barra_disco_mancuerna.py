import random

from modelos.barra_disco_mancuerna import BarraDiscoMancuerna
from config import (
    PESOS_BARRAS,
    PESOS_MANCUERNAS,
    PESOS_DISCOS
)


class GeneradorBarraDiscoMancuerna:

    def generar(self, equipamientos):

        barras_discos_mancuernas = []

        for equipamiento in equipamientos:

            if equipamiento.idTipoEquipamiento not in (2, 3, 4):
                continue

            barras_discos_mancuernas.append(
                BarraDiscoMancuerna(
                    codigoEquipamiento=equipamiento.codigoEquipamiento,
                    pesoKg=self._generar_peso(
                        equipamiento.idTipoEquipamiento
                    )
                )
            )

        return barras_discos_mancuernas

    def _generar_peso(self, tipo):

        if tipo == 2:
            return random.choice(PESOS_BARRAS)

        if tipo == 3:
            return random.choice(PESOS_MANCUERNAS)

        return random.choice(PESOS_DISCOS)