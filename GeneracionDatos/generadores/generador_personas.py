from faker import Faker
import random
from datetime import date, timedelta
from modelos.persona import Persona
from config import (
    CALLES,
    CODIGO_POSTAL,
    DOMINIOS_EMAIL,
    DISTRIBUCION_EDADES,
    PROBABILIDAD_DEPARTAMENTO
)


class GeneradorPersonas:

    def __init__(self):
        self.fake = Faker("es_AR")

        self.dnis_utilizados = set()
        self.telefonos_utilizados = set()
        self.correos_utilizados = set()
        self.domicilios_generados = []

        Faker.seed(1234)
        random.seed(1234)

    def _generar_dni(self):
        while True:
            dni = random.randint(30_000_000, 49_000_000)
            if dni not in self.dnis_utilizados:
                self.dnis_utilizados.add(dni)
                return dni

    def _generar_nombre(self):
        return self.fake.first_name()

    def _generar_apellido(self):
        return self.fake.last_name()

    def _generar_fecha_nacimiento(self):
        rangos = list(DISTRIBUCION_EDADES.keys())
        pesos = list(DISTRIBUCION_EDADES.values())
        rango = random.choices(rangos, weights=pesos, k=1)[0]
        edad = random.randint(rango[0], rango[1])
        hoy = date.today()
        dias = edad * 365 + random.randint(0, 364)
        return hoy - timedelta(days=dias)

    def _generar_telefono(self):
        while True:
            telefono = "11" + str(random.randint(10000000, 99999999))
            if telefono not in self.telefonos_utilizados:
                self.telefonos_utilizados.add(telefono)
                return telefono

    def _generar_correo(self, nombre, apellido):
        while True:
            dominio = random.choice(DOMINIOS_EMAIL)
            numero = random.randint(1,999)
            correo = (
                f"{nombre}.{apellido}{numero}@{dominio}"
            ).lower()
            correo = correo.replace(" ", "")
            if correo not in self.correos_utilizados:
                self.correos_utilizados.add(correo)
                return correo

    def _generar_domicilio(self):
        domicilio = {
        "direccion": random.choice(CALLES),
        "numero": random.randint(100, 4500),
        "piso": None,
        "codigo_postal": CODIGO_POSTAL
        }
        if random.random() < PROBABILIDAD_DEPARTAMENTO:
            domicilio["piso"] = random.randint(1,12)
        return domicilio

    def generar_persona(self):
        nombre = self._generar_nombre()
        apellido = self._generar_apellido()

        domicilio = self._generar_domicilio()

        return Persona(
            dni=self._generar_dni(),
            nombre=nombre,
            apellido=apellido,
            fechaNacimiento=self._generar_fecha_nacimiento(),
            telefono=self._generar_telefono(),
            correoElectronico=self._generar_correo(nombre, apellido),
            direccionDomicilio=domicilio["direccion"],
            numeroDomicilio=domicilio["numero"],
            pisoDomicilio=domicilio["piso"],
            codigoPostalDomicilio=domicilio["codigo_postal"]
        )