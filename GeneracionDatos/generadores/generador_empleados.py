import random
from datetime import timedelta, date

from config import (
    FECHA_APERTURA,
    FECHA_ACTUAL,
    EMPLEADOS_POR_TURNO,
    EMPLEADOS_EXTRA,
    DISTRIBUCION_EDADES_EMPLEADOS
)

from modelos.empleado import Empleado

class GeneradorEmpleados:

    def __init__(self, generador_personas):

        self.generador_personas = generador_personas
        self.proximo_legajo = 1

    def _generar_fecha_ingreso(self):

        probabilidad = random.random()

        if probabilidad < 0.70:

            inicio = FECHA_APERTURA
            fin = FECHA_APERTURA + timedelta(days=90)

        elif probabilidad < 0.90:

            inicio = FECHA_APERTURA + timedelta(days=91)
            fin = FECHA_APERTURA + timedelta(days=270)

        else:

            inicio = FECHA_APERTURA + timedelta(days=271)
            fin = FECHA_ACTUAL

        dias = random.randint(0, (fin - inicio).days)

        return inicio + timedelta(days=dias)

    def _generar_edad(self):

        rangos = list(DISTRIBUCION_EDADES_EMPLEADOS.keys())
        probabilidades = list(DISTRIBUCION_EDADES_EMPLEADOS.values())

        rango = random.choices(rangos, weights=probabilidades, k=1)[0]

        return random.randint(rango[0], rango[1])

    def _generar_fecha_nacimiento(self):

        edad = self._generar_edad()

        hoy = date.today()

        año = hoy.year - edad
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)

        return date(año, mes, dia)
    
    def _generar_empleado(self, id_cargo, id_turno):

        persona = self.generador_personas.generar_persona()
        persona.fechaNacimiento = self._generar_fecha_nacimiento()

        return Empleado(
            legajo=self.proximo_legajo,
            persona=persona,
            fechaIngreso=self._generar_fecha_ingreso(),
            idCargo=id_cargo,
            idTurno=id_turno
        )
    
    def generar(self):

        empleados = []

        for id_turno, cargos in EMPLEADOS_POR_TURNO.items():

            for id_cargo, cantidad in cargos.items():

                for _ in range(cantidad):

                    empleados.append(
                        self._generar_empleado(
                            id_cargo,
                            id_turno
                        )
                    )

                    self.proximo_legajo += 1
        
        for id_cargo, cantidad in EMPLEADOS_EXTRA.items():

            for _ in range(cantidad):

                empleados.append(

                    self._generar_empleado(
                        id_cargo,
                        random.randint(1, 3)
                    )

                )

                self.proximo_legajo += 1

        return empleados