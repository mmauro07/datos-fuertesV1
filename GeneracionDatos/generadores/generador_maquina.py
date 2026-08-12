from modelos.maquina import Maquina
from config import MAQUINAS


class GeneradorMaquinas:

    def generar(self, equipamientos):

        maquinas = []

        maquinas_config = []

        for nombre, descripcion, cantidad in MAQUINAS:
            for _ in range(cantidad):
                maquinas_config.append((nombre, descripcion))

        indice = 0

        for equipamiento in equipamientos:

            if equipamiento.idTipoEquipamiento != 1:
                continue

            nombre, descripcion = maquinas_config[indice]

            maquinas.append(
                Maquina(
                    codigoEquipamiento=equipamiento.codigoEquipamiento,
                    nombre=nombre,
                    descripcion=descripcion
                )
            )

            indice += 1

        return maquinas