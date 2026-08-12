from datetime import datetime, timedelta
import random
from config import PERFILES_ASISTENCIA
from modelos.fichada_socio import FichadaSocio

class GeneradorFichadasSocios:

    def __init__(self):

        self.perfiles = {}

    def _crear_indice_aptos(self, aptos_fisicos):

        return {
            apto.dniSocio: apto
            for apto in aptos_fisicos
        }
    
    def _cantidad_fichadas(self):

        return random.randint(8, 18)
    
    def _generar_hora(self):

        hora = random.randint(6, 21)

        minuto = random.randint(0, 59)

        segundo = random.randint(0, 59)

        return hora, minuto, segundo
    
    def _generar_fechas(self,
                    fecha_inicio,
                    fecha_fin,
                    cantidad):

        dias_disponibles = (
            fecha_fin - fecha_inicio
        ).days + 1

        cantidad = min(cantidad, dias_disponibles)

        dias = random.sample(
            range(dias_disponibles),
            cantidad
        )

        dias.sort()

        return [
            fecha_inicio + timedelta(days=d)
            for d in dias
        ]
    

    def _obtener_perfil(self, dni):

        if dni in self.perfiles:
            return self.perfiles[dni]

        nombres = list(PERFILES_ASISTENCIA.keys())
        pesos = [
            PERFILES_ASISTENCIA[p]["probabilidad"]
            for p in nombres
        ]

        perfil = random.choices(
            nombres,
            weights=pesos,
            k=1
        )[0]

        self.perfiles[dni] = perfil

        return perfil
    
    def _cantidad_fichadas(self, dni):

        perfil = self._obtener_perfil(dni)

        datos = PERFILES_ASISTENCIA[perfil]

        return random.randint(
            datos["min"],
            datos["max"]
        )

    def generar(
        self,
        membresias,
        aptos_fisicos
    ):
        indice_aptos = self._crear_indice_aptos(
        aptos_fisicos
        )

        fichadas = []

        for membresia in membresias:

            apto = indice_aptos.get(
                membresia.dniSocio
            )

            if apto is None:
                continue

            inicio = max(
            membresia.fechaInicio,
            apto.fechaPresentacion
            )

            fin = membresia.fechaFin

            if inicio > fin:
                continue

            cantidad = self._cantidad_fichadas(
                            membresia.dniSocio
                        )

            fechas = self._generar_fechas(
                                inicio,
                                fin,
                                cantidad
                            )
            
            for fecha in fechas:

                hora, minuto, segundo = (
                    self._generar_hora()
                )

                fichadas.append(
                    FichadaSocio(
                        dni=membresia.dniSocio,
                        fechaHora=datetime(
                            fecha.year,
                            fecha.month,
                            fecha.day,
                            hora,
                            minuto,
                            segundo
                        )
                    )
                )

        return fichadas