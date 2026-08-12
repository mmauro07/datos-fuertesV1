import random
from datetime import date

from dateutil.relativedelta import relativedelta

from config import (
    PROBABILIDAD_RENOVACION,
    PROBABILIDADES_MEDIO_PAGO,
    PROBABILIDADES_TIPO_MEMBRESIA
)

from modelos.membresia import Membresia

class GeneradorMembresias:

    def __init__(self):
        pass

    def _generar_tipo_membresia(self):

        tipos = list(PROBABILIDADES_TIPO_MEMBRESIA.keys())
        pesos = list(PROBABILIDADES_TIPO_MEMBRESIA.values())

        return random.choices(tipos, weights=pesos, k=1)[0]
    
    def _generar_medio_pago(self):

        medios = list(PROBABILIDADES_MEDIO_PAGO.keys())
        pesos = list(PROBABILIDADES_MEDIO_PAGO.values())

        return random.choices(medios, weights=pesos, k=1)[0]
    
    def _renueva(self):

        return random.random() < PROBABILIDAD_RENOVACION
    
    def generar_membresias(self, socio):

        historial = []

        fecha_inicio = socio.fechaAlta

        tipo_membresia = self._generar_tipo_membresia()

        hoy = date.today()

        while fecha_inicio <= hoy:

            fecha_fin = fecha_inicio + relativedelta(months=1)

            historial.append(
                Membresia(
                    dniSocio=socio.persona.dni,
                    fechaInicio=fecha_inicio,
                    fechaFin=fecha_fin,
                    idTipoMembresia=tipo_membresia,
                    idMedioPago=self._generar_medio_pago()
                )
            )

            if not self._renueva():
                break

            fecha_inicio = fecha_fin

        return historial
    
    def generar(self, socios):

        membresias = []

        for socio in socios:

            membresias.extend(
                self.generar_membresias(socio)
            )

        return membresias