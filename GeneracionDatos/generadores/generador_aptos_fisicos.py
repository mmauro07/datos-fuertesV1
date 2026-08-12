import random
from datetime import timedelta

from config import PROBABILIDAD_APTO_FISICO
from modelos.apto_fisico import AptoFisico


class GeneradorAptosFisicos:

    def __init__(self):
        pass

    def _generar_fecha_presentacion(self, fecha_alta):

        dias = random.randint(0, 30)

        return fecha_alta + timedelta(days=dias)

    def generar_apto_fisico(self, socio):

        if random.random() > PROBABILIDAD_APTO_FISICO:
            return None

        fecha_presentacion = self._generar_fecha_presentacion(
            socio.fechaAlta
        )

        fecha_vencimiento = fecha_presentacion + timedelta(days=365)

        return AptoFisico(
            dniSocio=socio.persona.dni,
            fechaPresentacion=fecha_presentacion,
            fechaVencimiento=fecha_vencimiento
        )

    def generar(self, socios):

        aptos_fisicos = []

        for socio in socios:

            apto = self.generar_apto_fisico(socio)

            if apto is not None:
                aptos_fisicos.append(apto)

        return aptos_fisicos