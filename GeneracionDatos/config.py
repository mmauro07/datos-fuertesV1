from datetime import date

FECHA_APERTURA = date(2025, 10, 6)
FECHA_ACTUAL = date.today()

PROBABILIDAD_APTO_FISICO = 0.95

PROBABILIDAD_RENOVACION = 0.90

PROBABILIDADES_TIPO_MEMBRESIA = {
    1: 0.75,   # Regular
    2: 0.15,   # Estudiantil
    3: 0.10    # Jubilado
}

PROBABILIDADES_MEDIO_PAGO = {
    1: 0.10,   # Efectivo
    2: 0.40,   # Débito
    3: 0.30,   # Crédito
    4: 0.20    # Transferencia
}

ID_MEDIO_PAGO_EFECTIVO = 1

PRECIOS_MEMBRESIA = {
    1: 50000.00,   # Regular
    2: 40000.00,   # Estudiantil
    3: 35000.00    # Jubilado
}

IMPORTES_RECIBIDOS = {
    50000: {
        50000: 0.60,
        60000: 0.30,
        70000: 0.10
    },

    40000: {
        40000: 0.55,
        50000: 0.30,
        60000: 0.15
    },

    35000: {
        35000: 0.50,
        40000: 0.20,
        50000: 0.20,
        60000: 0.10
    }
}

CALLES = [
    "Los Tilos",
    "Los Ceibos",
    "Los Aromos",
    "Las Acacias",
    "Los Fresnos",
    "Los Robles",
    "Los Álamos",
    "Los Sauces",
    "Los Ombúes",
    "Los Lapachos",
    "Las Tipas",
    "Los Cipreses",
    "Los Plátanos",
    "Las Magnolias",
    "Las Camelias",
    "Las Violetas",
    "Las Azaleas",
    "Los Pinos",
    "Los Eucaliptos",
    "Los Olivos",
    "Los Arrayanes",
    "Los Espinillos",
    "Los Jacarandás",
    "Los Abedules",
    "Los Paraísos",
    "Los Nogales",
    "Los Castaños",
    "Los Tamariscos",
    "Los Cedros",
    "Las Orquídeas"
]

CODIGO_POSTAL = 1700

DOMINIOS_EMAIL = [
    "gmail.com",
    "hotmail.com",
    "outlook.com",
    "yahoo.com.ar"
]

DISTRIBUCION_EDADES = {
    (12, 17): 8,
    (18, 25): 35,
    (26, 35): 27,
    (36, 50): 18,
    (51, 65): 9,
    (66, 80): 3
}

ALTAS_POR_MES = {
    (2025, 10): 4,
    (2025, 11): 12,
    (2025, 12): 18,
    (2026, 1): 58,
    (2026, 2): 46,
    (2026, 3): 28,
    (2026, 4): 18,
    (2026, 5): 10,
    (2026, 6): 4,
    (2026, 7): 2
}

PROBABILIDAD_DEPARTAMENTO = 0.30

PROBABILIDAD_COMPARTIR_DOMICILIO = 0.15

PERFILES_ASISTENCIA = {
    "baja": {
        "probabilidad": 0.20,
        "min": 4,
        "max": 8
    },
    "media": {
        "probabilidad": 0.60,
        "min": 9,
        "max": 14
    },
    "alta": {
        "probabilidad": 0.20,
        "min": 15,
        "max": 22
    }
}

EMPLEADOS_POR_TURNO = {
    1: {  # Mañana
        1: 2,  # Entrenador
        2: 1,  # Recepcionista
        3: 1   # Limpieza
    },
    2: {  # Tarde
        1: 2,
        2: 1,
        3: 1
    },
    3: {  # Noche
        1: 2,
        2: 1,
        3: 1
    }
}

EMPLEADOS_EXTRA = {
    1: 2,  # Entrenadores
    2: 1,  # Recepcionistas
    3: 1   # Limpieza
}

DISTRIBUCION_EDADES_EMPLEADOS = {
    (18, 25): 0.20,
    (26, 35): 0.40,
    (36, 45): 0.25,
    (46, 55): 0.10,
    (56, 65): 0.05
}

DISTRIBUCION_ESTADOS_EMPLEADO = {
    1: 0.85,   # Activo
    2: 0.10,   # En licencia
    3: 0.05    # Renunció
}

MOTIVOS_LICENCIA = [
    "Enfermedad",
    "Accidente",
    "Maternidad",
    "Paternidad",
    "Estudio",
    "Vacaciones prolongadas",
    "Motivos personales"
]

HORARIOS_TURNO = {
    1: {  # Mañana
        "entrada": (5, 45, 6, 15),
        "salida": (13, 45, 14, 15)
    },
    2: {  # Tarde
        "entrada": (13, 45, 14, 15),
        "salida": (21, 45, 22, 15)
    },
    3: {  # Noche
        "entrada": (21, 45, 22, 15),
        "salida": (5, 45, 6, 15)
    }
}

PROBABILIDAD_ASISTENCIA = 0.90

SUELDOS_BASE = {
    1: 1800000,   # Entrenador
    2: 1500000,   # Recepcionista
    3: 1200000    # Limpieza
}

ADICIONAL_TURNO = {
    1: 0.00,      # Mañana
    2: 0.05,      # Tarde
    3: 0.10       # Noche
}

ADICIONAL_ANTIGUEDAD = 0.01

DISTRIBUCION_OBJETIVOS = {
    1: 0.40,   # Hipertrofia
    2: 0.20,   # Fuerza
    3: 0.20,   # Descenso de peso
    4: 0.15,   # Resistencia
    5: 0.05    # Rehabilitación
}

PROBABILIDAD_NUEVA_RUTINA = 0.30

OBSERVACIONES_RUTINA = [
    None,
    None,
    None,
    "Aumentar carga progresivamente.",
    "Priorizar técnica.",
    "Realizar movilidad antes de entrenar.",
    "Respetar tiempos de descanso.",
    "Controlar la intensidad."
]

CANTIDAD_EQUIPAMIENTO = {
    1: 25,   # Máquina
    2: 12,   # Barra
    3: 40,   # Mancuerna
    4: 80,   # Disco
    5: 12,   # Banco
    6: 20,   # Colchoneta
    7: 16,   # Kettlebell
    8: 20    # Banda elástica
}

MODELOS = list(range(1, 21))

DISTRIBUCION_ADQUISICION_EQUIPAMIENTO = {
    "antes_apertura": 0.30,
    "fin_2025": 0.35,
    "primer_trimestre_2026": 0.25,
    "reciente": 0.10
}

PESOS_BARRAS = [
    10,
    15,
    20
]

PESOS_MANCUERNAS = [
    2.5,
    5,
    7.5,
    10,
    12.5,
    15,
    17.5,
    20,
    22.5,
    25,
    30,
    35,
    40
]

PESOS_DISCOS = [
    1.25,
    2.5,
    5,
    10,
    15,
    20
]

MAQUINAS = [
    (
        "Prensa 45°",
        "Máquina para el entrenamiento de piernas enfocada en cuádriceps glúteos e isquiotibiales.",
        2
    ),
    (
        "Jalón al pecho",
        "Permite trabajar principalmente el dorsal ancho mediante un movimiento de tracción vertical.",
        3
    ),
    (
        "Remo sentado",
        "Máquina destinada al fortalecimiento de la musculatura de la espalda.",
        2
    ),
    (
        "Press de pecho",
        "Trabaja pectorales tríceps y deltoides anteriores.",
        2
    ),
    (
        "Press inclinado",
        "Enfatiza la porción superior del pectoral.",
        1
    ),
    (
        "Press de hombros",
        "Desarrolla los deltoides y los tríceps.",
        1
    ),
    (
        "Extensión de piernas",
        "Ejercicio de aislamiento para cuádriceps.",
        2
    ),
    (
        "Camilla femoral",
        "Trabaja principalmente los isquiotibiales.",
        2
    ),
    (
        "Aductor",
        "Fortalece los músculos aductores de la cadera.",
        1
    ),
    (
        "Abductor",
        "Fortalece los músculos abductores de la cadera.",
        1
    ),
    (
        "Polea alta",
        "Permite realizar múltiples ejercicios para espalda brazos y hombros.",
        2
    ),
    (
        "Polea baja",
        "Utilizada para ejercicios de remo bíceps y otros movimientos de tracción.",
        1
    ),
    (
        "Cruce de poleas",
        "Equipo multifunción para ejercicios de pecho hombros y brazos.",
        1
    ),
    (
        "Smith",
        "Barra guiada para realizar ejercicios con mayor estabilidad.",
        1
    ),
    (
        "Hack squat",
        "Máquina para sentadillas guiadas enfocadas en piernas.",
        1
    ),
    (
        "Pantorrillera",
        "Diseñada para el trabajo específico de los gemelos.",
        1
    ),
    (
        "Fondos asistidos",
        "Asiste en la ejecución de fondos y dominadas.",
        1
    ),
    (
        "Abdominales",
        "Máquina para fortalecer la musculatura abdominal.",
        1
    ),
    (
        "Lumbar",
        "Trabaja la zona baja de la espalda.",
        1
    ),
    (
        "Pec Deck",
        "Máquina para aperturas de pecho.",
        1
    )
]

PROBABILIDAD_SOLICITUD = {
    1: 0.35,   # Máquina
    2: 0.15,   # Barra
    3: 0.10,   # Mancuerna
    4: 0.05,   # Disco
    5: 0.08,   # Banco
    6: 0.03,   # Colchoneta
    7: 0.08,   # Kettlebell
    8: 0.05    # Banda elástica
}

DESCRIPCIONES_PROBLEMAS = [
    "Se detectó desgaste por uso.",
    "Presenta un funcionamiento irregular.",
    "Se observan ruidos durante su utilización.",
    "Se aflojaron componentes estructurales.",
    "Presenta desgaste en el sistema de poleas.",
    "El tapizado está deteriorado.",
    "El sistema de regulación no funciona correctamente.",
    "Se detectó una falla mecánica.",
    "Requiere inspección preventiva.",
    "Se recomienda mantenimiento general."
]

PROBABILIDAD_MANTENIMIENTO_REALIZADO = 0.90

DIAS_REPARACION = (1, 15)

COSTOS_REPARACION = [
    (None, 0.10),   # Garantía / ajuste menor
    (5000, 0.20),
    (10000, 0.30),
    (20000, 0.25),
    (35000, 0.10),
    (50000, 0.05)
]

PROBABILIDAD_FUERA_SERVICIO = 0.02

EJERCICIOS = [
    (
        "Press de banca con barra",
        "Empuje horizontal con barra para desarrollar el pecho.",
        1, 2, 1
    ),
    (
        "Press inclinado con mancuernas",
        "Trabaja principalmente la porción superior del pecho.",
        1, 2, 1
    ),
    (
        "Aperturas con mancuernas",
        "Aislamiento del pectoral mediante apertura de brazos.",
        1, 1, 1
    ),
    (
        "Aperturas en Pec Deck",
        "Ejercicio de aislamiento para el pecho utilizando máquina.",
        1, 1, 1
    ),
    (
        "Fondos en paralelas",
        "Empuje con peso corporal enfocado en pecho y tríceps.",
        1, 3, 1
    ),
    (
        "Flexiones de brazos",
        "Ejercicio clásico de empuje con peso corporal.",
        1, 1, 1
    ),
    (
        "Jalón al pecho",
        "Tracción vertical para desarrollar la espalda.",
        2, 1, 1
    ),
    (
        "Dominadas",
        "Tracción con peso corporal enfocada en dorsales.",
        2, 3, 1
    ),
    (
        "Remo sentado",
        "Remo horizontal utilizando máquina.",
        2, 2, 1
    ),
    (
        "Remo con barra",
        "Ejercicio libre para desarrollar la espalda media.",
        2, 3, 1
    ),
    (
        "Remo con mancuerna",
        "Remo unilateral para dorsales.",
        2, 2, 1
    ),
    (
        "Pullover en polea",
        "Extensión de hombros enfocada en dorsales.",
        2, 2, 1
    ),
    (
        "Peso muerto",
        "Ejercicio compuesto para la cadena posterior.",
        2, 3, 1
    ),
    (
        "Hiperextensiones lumbares",
        "Fortalece la zona lumbar y la cadena posterior.",
        2, 1, 1
    ),
    (
        "Press militar",
        "Empuje vertical para hombros.",
        3, 2, 1
    ),
    (
        "Press Arnold",
        "Variante del press con rotación de hombros.",
        3, 2, 1
    ),
    (
        "Elevaciones laterales",
        "Aislamiento del deltoides medio.",
        3, 1, 1
    ),
    (
        "Elevaciones frontales",
        "Trabajo del deltoides anterior.",
        3, 1, 1
    ),
    (
        "Pájaros con mancuernas",
        "Trabajo del deltoides posterior.",
        3, 2, 1
    ),
    (
        "Curl con barra",
        "Curl tradicional para bíceps.",
        4, 2, 1
    ),
    (
        "Curl con mancuernas",
        "Curl alternado para bíceps.",
        4, 1, 1
    ),
    (
        "Curl martillo",
        "Curl con agarre neutro para bíceps y braquial.",
        4, 1, 1
    ),
    (
        "Curl en banco Scott",
        "Curl de aislamiento para bíceps.",
        4, 2, 1
    ),
    (
        "Curl en polea",
        "Curl utilizando polea baja.",
        4, 2, 1
    ),
    (
        "Press francés",
        "Extensión de tríceps con barra.",
        5, 2, 1
    ),
    (
        "Extensión de tríceps en polea",
        "Trabajo de tríceps mediante polea.",
        5, 1, 1
    ),
    (
        "Extensión sobre la cabeza",
        "Trabajo de la cabeza larga del tríceps.",
        5, 2, 1
    ),
    (
        "Fondos en banco",
        "Trabajo de tríceps utilizando un banco.",
        5, 1, 1
    ),
    (
        "Patada de tríceps",
        "Extensión unilateral con mancuerna.",
        5, 2, 1
    ),
    (
        "Curl de muñeca",
        "Flexión de muñeca para fortalecer antebrazos.",
        6, 1, 1
    ),
    (
        "Curl inverso",
        "Trabajo de extensores del antebrazo.",
        6, 2, 1
    ),
    (
        "Farmer's Walk",
        "Caminata con carga para fortalecer agarre y antebrazos.",
        6, 2, 1
    ),
    (
        "Crunch abdominal",
        "Flexión de tronco para fortalecer el abdomen.",
        7, 1, 1
    ),
    (
        "Crunch en máquina",
        "Trabajo abdominal utilizando máquina.",
        7, 1, 1
    ),
    (
        "Elevación de piernas",
        "Trabajo del abdomen inferior.",
        7, 2, 1
    ),
    (
        "Plancha",
        "Ejercicio isométrico para fortalecer el core.",
        7, 1, 3
    ),
    (
        "Russian Twist",
        "Rotación del tronco para trabajar oblicuos.",
        7, 2, 1
    ),
    (
        "Mountain Climbers",
        "Ejercicio cardiovascular con trabajo abdominal.",
        7, 2, 2
    ),
    (
        "Sentadilla con barra",
        "Ejercicio compuesto para piernas.",
        8, 3, 1
    ),
    (
        "Prensa inclinada",
        "Trabajo guiado de cuádriceps.",
        8, 1, 1
    ),
    (
        "Sentadilla Hack",
        "Variante guiada de sentadilla.",
        8, 2, 1
    ),
    (
        "Extensión de piernas",
        "Aislamiento de cuádriceps.",
        8, 1, 1
    ),
    (
        "Zancadas",
        "Trabajo unilateral de piernas.",
        8, 2, 1
    ),
    (
        "Sentadilla búlgara",
        "Ejercicio unilateral avanzado.",
        8, 3, 1
    ),
    (
        "Peso muerto rumano",
        "Trabajo de isquiotibiales.",
        9, 3, 1
    ),
    (
        "Curl femoral",
        "Flexión de rodilla en máquina.",
        9, 1, 1
    ),
    (
        "Buenos días",
        "Ejercicio para la cadena posterior.",
        9, 3, 1
    ),
    (
        "Puente de glúteos",
        "Extensión de cadera con peso corporal.",
        10, 1, 1
    ),
    (
        "Hip Thrust",
        "Empuje de cadera con barra.",
        10, 2, 1
    ),
    (
        "Patada de glúteo en polea",
        "Trabajo aislado de glúteos.",
        10, 1, 1
    ),
    (
        "Abducción de cadera",
        "Trabajo del glúteo medio.",
        10, 1, 1
    ),
    (
        "Elevación de talones de pie",
        "Trabajo de gemelos de pie.",
        11, 1, 1
    ),
    (
        "Elevación de talones sentado",
        "Trabajo específico del sóleo.",
        11, 1, 1
    ),
    (
        "Movilidad de hombros con banda elástica",
        "Ejercicio para mejorar la movilidad del hombro.",
        3, 1, 3
    ),
    (
        "Estiramiento dinámico de cuerpo completo",
        "Rutina de movilidad y flexibilidad general.",
        7, 1, 4
    )
]

OBSERVACIONES_DETALLE_RUTINA = [
    None,
    None,
    None,
    "Mantener la técnica durante todo el ejercicio.",
    "Controlar la velocidad de ejecución.",
    "Realizar el movimiento completo.",
    "Evitar impulsos.",
    "Aumentar el peso si completa todas las series.",
    "Reducir el peso si pierde la técnica."
]