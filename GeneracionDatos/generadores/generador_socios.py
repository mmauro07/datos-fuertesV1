import random
from calendar import monthrange
from datetime import date

from config import ALTAS_POR_MES
from generadores.generador_personas import GeneradorPersonas
from modelos.socio import Socio


class GeneradorSocios:

    def __init__(self, generador_personas: GeneradorPersonas):
        self.generador_personas = generador_personas
        self.altas_pendientes = self._crear_calendario_altas()

    def _generar_dia_del_mes(self, anio: int, mes: int) -> int:
        ultimo_dia = monthrange(anio, mes)[1]
        # El gimnasio abrió el 6 de octubre de 2025
        primer_dia = 6 if (anio == 2025 and mes == 10) else 1
        franjas = []
        pesos = []
        # Primera franja
        inicio = primer_dia
        fin = min(10, ultimo_dia)
        if inicio <= fin:
            franjas.append((inicio, fin))
            pesos.append(60)
        # Segunda franja
        inicio = max(11, primer_dia)
        fin = min(20, ultimo_dia)
        if inicio <= fin:
            franjas.append((inicio, fin))
            pesos.append(30)
        # Tercera franja
        inicio = max(21, primer_dia)
        fin = ultimo_dia
        if inicio <= fin:
            franjas.append((inicio, fin))
            pesos.append(10)
        franja = random.choices(franjas, weights=pesos, k=1)[0]
        return random.randint(franja[0], franja[1])

    def _crear_calendario_altas(self):
        altas = []
        for (anio, mes), cantidad in ALTAS_POR_MES.items():
            for _ in range(cantidad):
                dia = self._generar_dia_del_mes(anio, mes)
                altas.append(date(anio, mes, dia))
        random.shuffle(altas)
        return altas

    def _generar_fecha_alta(self):
        if not self.altas_pendientes:
            raise ValueError("No quedan fechas de alta disponibles.")
        return self.altas_pendientes.pop()

    def generar_socio(self):
        persona = self.generador_personas.generar_persona()
        return Socio(
            persona=persona,
            fechaAlta=self._generar_fecha_alta()
        )
    
    def generar(self, cantidad):
        return [
            self.generar_socio()
            for _ in range(cantidad)
        ]