# Datos Fuertes

**Datos Fuertes** es un proyecto de base de datos para la gestión integral de un gimnasio ficticio de una sola sede. El proyecto fue diseñado como una aplicación práctica de los contenidos de la Tecnicatura Universitaria en Gestión y Análisis de Datos en Organizaciones.

La primera versión del proyecto se centra en el **diseño relacional, la implementación en SQL Server y la generación automatizada de datos sintéticos con Python**.

> **Versión actual:** V1.0.0

## Objetivos

El proyecto busca modelar y poblar un sistema que permita gestionar, entre otros aspectos:

- Socios y sus datos personales.
- Membresías, pagos y fichadas.
- Aptos físicos.
- Empleados, cargos, turnos y estados laborales.
- Licencias, fichadas y liquidaciones de sueldos.
- Rutinas de entrenamiento y sus detalles.
- Equipamiento, máquinas y estados del equipamiento.
- Solicitudes y trabajos de mantenimiento.
- Ejercicios y sus relaciones con equipamiento y máquinas.

La generación de datos se realiza de forma sintética, aplicando reglas de negocio y manteniendo la integridad referencial del modelo.

## Tecnologías

- **SQL Server 2025**
- **Python 3.12**
- **pandas**
- **Faker**
- **Git / GitHub**

## Estructura del proyecto

```text
datos-fuertesV1/
│
├── SQL/
│   ├── CreacionTablas.sql
│   ├── Procedimientos.sql
│   └── ...
│
├── GeneracionDatos/
│   ├── main.py
│   ├── CargaInicial.py
│   ├── config.py
│   ├── tipos_sql.py
│   ├── exportador.py
│   │
│   ├── modelos/
│   │   └── ...
│   │
│   └── generadores/
│       └── ...
│
├── README.md
└── .gitignore
```

## Arquitectura de generación

La generación de datos está separada del proceso de carga en SQL Server.

```text
Configuración + modelos + generadores
                │
                ▼
             main.py
                │
                ▼
          Archivos CSV
                │
                ▼
        CargaInicial.py
                │
                ▼
          SQL Server 2025
```

### Python

Python se utiliza para generar los datos sintéticos. Los generadores están separados por entidad y utilizan modelos `dataclass` para representar los registros antes de exportarlos.

Los identificadores artificiales de las tablas principales son generados desde Python. Esto permite que las claves estén disponibles desde el momento en que se crean los objetos y simplifica la generación de las tablas dependientes.

Las tablas tipificadas utilizan identificadores definidos por sus datos iniciales.

### SQL Server

SQL Server se encarga de:

- Implementar el modelo relacional.
- Aplicar claves primarias y foráneas.
- Aplicar restricciones `CHECK` y `UNIQUE`.
- Mantener la integridad referencial.
- Ejecutar procedimientos y lógica propia de base de datos.

## Datos generados

La V1 incluye generación para las principales entidades y procesos del gimnasio, entre ellos:

- Socio
- AptoFisico
- Membresia
- PagoEfectivo
- FichadaSocio
- Empleado
- EstadoEmpleado
- LicenciaEmpleado
- Recepcionista
- FichadaEmpleado
- LiquidacionSueldos
- Rutina
- DetalleRutina
- Equipamiento
- BarraDiscoMancuerna
- Maquina
- SolicitudMantenimiento
- MantenimientoHecho
- EstadoEquipamiento
- Ejercicio

Las tablas de relación que representan conocimiento fijo del dominio, como `MaquinaEjercicio` y `EquipamientoEjercicio`, se cargan mediante scripts SQL en lugar de generarse aleatoriamente.

## Cómo ejecutar el proyecto

### 1. Requisitos

Instalar:

- SQL Server 2025.
- Python 3.12.
- Git.

Las dependencias de Python utilizadas por el proyecto pueden instalarse mediante `pip` según las librerías importadas por la versión correspondiente del generador.

### 2. Crear la base de datos

Ejecutar el script de creación de tablas ubicado en `SQL/` sobre una instancia de SQL Server.

Las tablas tipificadas se inicializan mediante los `INSERT` incluidos en los scripts SQL.

### 3. Generar los datos

Desde la carpeta `GeneracionDatos` ejecutar:

```powershell
python main.py
```

El programa genera los archivos CSV correspondientes a las entidades del proyecto.

### 4. Cargar los datos

Una vez generados los CSV, ejecutar:

```powershell
python CargaInicial.py
```

Este proceso carga los datos generados en SQL Server utilizando el procedimiento de importación definido en los scripts SQL.

### 5. Cargar relaciones manuales

Las relaciones fijas que no se generan aleatoriamente, como `MaquinaEjercicio` y `EquipamientoEjercicio`, se cargan mediante los scripts SQL correspondientes.

## Diseño y criterios de generación

El generador intenta mantener coherencia temporal y referencial. Algunos ejemplos:

- Una membresía pertenece a un socio existente.
- Un pago pertenece a una membresía existente.
- Una fichada se genera de acuerdo con la situación del socio.
- Las fichadas de empleados se relacionan con empleados existentes y consideran sus estados laborales.
- Las licencias son especializaciones de estados de empleados.
- Las rutinas pertenecen a socios y son asignadas por empleados que cumplen el rol correspondiente.
- Las solicitudes de mantenimiento se relacionan con equipamientos existentes.
- Los mantenimientos realizados dependen de solicitudes previamente generadas.
- Los estados del equipamiento se construyen a partir de su historial de mantenimiento.
- Los detalles de rutina utilizan ejercicios existentes.

El objetivo de la generación no es reproducir exactamente el funcionamiento de un gimnasio real, sino producir un conjunto de datos suficientemente consistente, variado y escalable para realizar consultas, análisis y pruebas posteriores.

## V1.0.0

La primera versión representa una **base funcional y poblada**, pensada como punto de partida para futuras etapas del proyecto.

Entre las siguientes posibilidades de expansión se encuentran:

- Historial de varios años de operación.
- Mayor volumen de socios y transacciones.
- Reportes y análisis descriptivos.
- Visualizaciones y dashboards.
- Análisis de retención y abandono de socios.
- Análisis temporal de ingresos y actividad.
- Segmentación de socios.
- Aplicaciones de machine learning.
- Nuevas consultas, vistas, procedimientos y triggers.

## Autor

**Mauro Costilla**

Proyecto académico y de práctica para la Tecnicatura Universitaria en Gestión y Análisis de Datos en Organizaciones.
