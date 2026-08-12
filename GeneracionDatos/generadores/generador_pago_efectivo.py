import random

from config import (
    ID_MEDIO_PAGO_EFECTIVO,
    PRECIOS_MEMBRESIA,
    IMPORTES_RECIBIDOS
)

from modelos.pago_efectivo import PagoEfectivo

class GeneradorPagoEfectivo:

    def __init__(self):
        pass

    def _generar_importe_recibido(self, precio):

        importes = list(IMPORTES_RECIBIDOS[precio].keys())
        probabilidades = list(IMPORTES_RECIBIDOS[precio].values())

        return random.choices(
            importes,
            weights=probabilidades,
            k=1
        )[0]
    
    def _generar_vuelto(self, importe_recibido, precio):

        return round(importe_recibido - precio, 2)
    
    def generar(self, membresias):

        pagos = []

        for membresia in membresias:

            if membresia.idMedioPago != ID_MEDIO_PAGO_EFECTIVO:
                continue

            precio = PRECIOS_MEMBRESIA[membresia.idTipoMembresia]

            importe_recibido = self._generar_importe_recibido(precio)

            vuelto = self._generar_vuelto(
                importe_recibido,
                precio
            )

            pagos.append(
                PagoEfectivo(
                    dniSocio=membresia.dniSocio,
                    fechaInicio=membresia.fechaInicio,
                    importeRecibido=importe_recibido,
                    vuelto=vuelto
                )
            )

        return pagos
    
    