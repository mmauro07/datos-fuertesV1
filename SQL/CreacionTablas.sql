Create database DatosFuertes
GO

use DatosFuertes

-- Voy a empezar a crear las tablas de tipos ya que son independientes
-- de las demás y son la base de las próximas entidades.

-- Voy a realizar la inserción de datos de forma directa en ellas ya que cuentan con muy pocos.

-- Entidad MedioPago

CREATE TABLE MedioPago (
    idMedioPago TINYINT IDENTITY(1,1),
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT PK_MedioPago
        PRIMARY KEY (idMedioPago),

    CONSTRAINT UQ_MedioPago_Nombre
        UNIQUE (nombre)
);

INSERT INTO MedioPago (nombre)
VALUES
('Efectivo'),
('Tarjeta de Débito'),
('Tarjeta de Crédito'),
('Transferencia');



-- Entidad TipoMembresia

CREATE TABLE TipoMembresia (
    idTipoMembresia TINYINT IDENTITY(1,1),
    nombre VARCHAR(20) NOT NULL,
    cuotaMensual DECIMAL(10,2) NOT NULL,

    CONSTRAINT PK_TipoMembresia
        PRIMARY KEY (idTipoMembresia),

    CONSTRAINT UQ_TipoMembresia_Nombre
        UNIQUE (nombre),

    CONSTRAINT CK_TipoMembresia_Cuota
        CHECK (cuotaMensual > 0)
);

INSERT INTO TipoMembresia (nombre, cuotaMensual)
VALUES
('Regular', 50000.00),
('Estudiantil', 40000.00),
('Jubilado', 35000.00);



-- Entidad GrupoMuscular

CREATE TABLE GrupoMuscular (
    idGrupoMuscular TINYINT IDENTITY(1,1),
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT PK_GrupoMuscular
        PRIMARY KEY (idGrupoMuscular),

    CONSTRAINT UQ_GrupoMuscular_Nombre
        UNIQUE (nombre)
);

INSERT INTO GrupoMuscular (nombre)
VALUES
('Pecho'),
('Espalda'),
('Hombros'),
('Bíceps'),
('Tríceps'),
('Antebrazos'),
('Abdomen'),
('Cuádriceps'),
('Isquiotibiales'),
('Glúteos'),
('Gemelos');



-- Entidad Objetivo

CREATE TABLE Objetivo (
    idObjetivo TINYINT IDENTITY(1,1),
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT PK_Objetivo
        PRIMARY KEY (idObjetivo),

    CONSTRAINT UQ_Objetivo_Nombre
        UNIQUE (nombre)
);

INSERT INTO Objetivo (nombre)
VALUES
('Hipertrofia'),
('Fuerza'),
('Descenso de peso'),
('Resistencia'),
('Rehabilitación');



-- Entidad TipoEjercicio

CREATE TABLE TipoEjercicio (
    idTipoEjercicio TINYINT IDENTITY(1,1),
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT PK_TipoEjercicio
        PRIMARY KEY (idTipoEjercicio),

    CONSTRAINT UQ_TipoEjercicio_Nombre
        UNIQUE (nombre)
);

INSERT INTO TipoEjercicio (nombre)
VALUES
('Fuerza'),
('Cardiovascular'),
('Movilidad'),
('Flexibilidad');



-- Entidad Dificultad

CREATE TABLE Dificultad (
    idDificultad TINYINT IDENTITY(1,1),
    nombre VARCHAR(20) NOT NULL,

    CONSTRAINT PK_Dificultad
        PRIMARY KEY (idDificultad),

    CONSTRAINT UQ_Dificultad_Nombre
        UNIQUE (nombre)
);

INSERT INTO Dificultad (nombre)
VALUES
('Principiante'),
('Intermedio'),
('Avanzado');



-- Entidad TipoEquipamiento

CREATE TABLE TipoEquipamiento (
    idTipoEquipamiento TINYINT IDENTITY(1,1),
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT PK_TipoEquipamiento
        PRIMARY KEY (idTipoEquipamiento),

    CONSTRAINT UQ_TipoEquipamiento_Nombre
        UNIQUE (nombre)
);

INSERT INTO TipoEquipamiento (nombre)
VALUES
('Máquina'),
('Barra'),
('Mancuerna'),
('Disco'),
('Banco'),
('Colchoneta'),
('Kettlebell'),
('Banda elástica');



-- Entidad EstadoEqLista

CREATE TABLE EstadoEqLista (
    idEstadoEq TINYINT IDENTITY(1,1),
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT PK_EstadoEqLista
        PRIMARY KEY (idEstadoEq),

    CONSTRAINT UQ_EstadoEqLista_Nombre
        UNIQUE (nombre)
);

INSERT INTO EstadoEqLista (nombre)
VALUES
('Disponible'),
('En mantenimiento'),
('Fuera de servicio');



-- Entidad TipoMovimiento

CREATE TABLE TipoMovimiento (
    idTipoMovimiento TINYINT IDENTITY(1,1),
    nombre VARCHAR(20) NOT NULL,

    CONSTRAINT PK_TipoMovimiento
        PRIMARY KEY (idTipoMovimiento),

    CONSTRAINT UQ_TipoMovimiento_Nombre
        UNIQUE (nombre)
);

INSERT INTO TipoMovimiento (nombre)
VALUES
('Entrada'),
('Salida');



-- Entidad Cargo

CREATE TABLE Cargo (
    idCargo TINYINT IDENTITY(1,1),
    nombre VARCHAR(30) NOT NULL,

    CONSTRAINT PK_Cargo
        PRIMARY KEY (idCargo),

    CONSTRAINT UQ_Cargo_Nombre
        UNIQUE (nombre)
);

INSERT INTO Cargo (nombre)
VALUES
('Entrenador'),
('Recepcionista'),
('Personal de limpieza');



-- Entidad Turno

CREATE TABLE Turno (
    idTurno TINYINT IDENTITY(1,1),
    nombre VARCHAR(20) NOT NULL,

    CONSTRAINT PK_Turno
        PRIMARY KEY (idTurno),

    CONSTRAINT UQ_Turno_Nombre
        UNIQUE (nombre)
);

INSERT INTO Turno (nombre)
VALUES
('Mañana'),
('Tarde'),
('Noche');



-- Entidad EstadoEmpLista

CREATE TABLE EstadoEmpLista (
    idEstadoEmp TINYINT IDENTITY(1,1),
    nombre VARCHAR(20) NOT NULL,

    CONSTRAINT PK_EstadoEmpLista
        PRIMARY KEY (idEstadoEmp),

    CONSTRAINT UQ_EstadoEmpLista_Nombre
        UNIQUE (nombre)
);

INSERT INTO EstadoEmpLista (nombre)
VALUES
('Activo'),
('En licencia'),
('Renunció');

-- Entidad Marca

CREATE TABLE Marca (
    idMarca SMALLINT IDENTITY(1,1),
    nombre VARCHAR(50) NOT NULL,

    CONSTRAINT PK_Marca
        PRIMARY KEY (idMarca),

    CONSTRAINT UQ_Marca_Nombre
        UNIQUE (nombre)
);

INSERT INTO Marca (nombre)
VALUES
('Technogym'),
('Life Fitness'),
('Matrix'),
('BH Fitness'),
('Athletic');



-- Entidad Modelo

CREATE TABLE Modelo (
    idModelo SMALLINT IDENTITY(1,1),
    nombre VARCHAR(50) NOT NULL,
    idMarca SMALLINT NOT NULL,

    CONSTRAINT PK_Modelo
        PRIMARY KEY (idModelo),

    CONSTRAINT FK_Modelo_Marca
        FOREIGN KEY (idMarca)
        REFERENCES Marca(idMarca),

    CONSTRAINT UQ_Modelo_Marca_Nombre
        UNIQUE (idMarca, nombre)
);

INSERT INTO Modelo (nombre, idMarca)
VALUES
-- Technogym
('Selection', 1),
('Pure Strength', 1),
('Excite', 1),
('Skill Line', 1),

-- Life Fitness
('Insignia', 2),
('Signature', 2),
('Hammer Strength', 2),
('Integrity', 2),

-- Matrix
('Ultra', 3),
('Versa', 3),
('Magnum', 3),
('Performance', 3),

-- BH Fitness
('Movemia', 4),
('Inertia', 4),
('LK Line', 4),
('Crystal', 4),

-- Athletic
('Advanced', 5),
('Extreme', 5),
('Evolution', 5),
('Professional', 5);



-- Voy a seguir con las entidades principales ya que los
-- principales procesos transaccionales dependen de ellas

-- A partir de ahora no voy a insertarles datos directamente,
-- sino que voy a armar solo los esquemas para poder insertar
-- filas más adelante con un script de Python.

-- Entidad Socio

CREATE TABLE Socio (
    dni CHAR(8) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    direccionDomicilio VARCHAR(100) NOT NULL,
    numeroDomicilio SMALLINT NOT NULL,
    pisoDomicilio TINYINT NULL,
    codPostalDomicilio CHAR(4) NOT NULL,
    fechaAlta DATE NOT NULL,

    CONSTRAINT PK_Socio
        PRIMARY KEY (dni),

    CONSTRAINT UQ_Socio_Correo
        UNIQUE (correo),

    CONSTRAINT CK_Socio_NumeroDomicilio
        CHECK (numeroDomicilio > 0),

    CONSTRAINT CK_Socio_CodPostal
        CHECK (codPostalDomicilio LIKE '[0-9][0-9][0-9][0-9]')
);



-- Entidad Empleado

CREATE TABLE Empleado (
    legajo INT NOT NULL,
    dni CHAR(8) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    direccionDomicilio VARCHAR(100) NOT NULL,
    numeroDomicilio SMALLINT NOT NULL,
    pisoDomicilio TINYINT NULL,
    codPostalDomicilio CHAR(4) NOT NULL,
    fechaIngreso DATE NOT NULL,
    idCargo TINYINT NOT NULL,
    idTurno TINYINT NOT NULL,

    CONSTRAINT PK_Empleado
        PRIMARY KEY (legajo),

    CONSTRAINT UQ_Empleado_DNI
        UNIQUE (dni),

    CONSTRAINT UQ_Empleado_Correo
        UNIQUE (correo),

    CONSTRAINT CK_Empleado_NumeroDomicilio
        CHECK (numeroDomicilio > 0),

    CONSTRAINT CK_Empleado_CodPostal
        CHECK (codPostalDomicilio LIKE '[0-9][0-9][0-9][0-9]'),

    CONSTRAINT FK_Empleado_Cargo
        FOREIGN KEY (idCargo)
        REFERENCES Cargo(idCargo),

    CONSTRAINT FK_Empleado_Turno
        FOREIGN KEY (idTurno)
        REFERENCES Turno(idTurno)
);



-- Entidad Recepcionista

CREATE TABLE Recepcionista (
    legajo INT NOT NULL,
    telCorpAsig VARCHAR(20) NOT NULL,

    CONSTRAINT PK_Recepcionista
        PRIMARY KEY(legajo),

    CONSTRAINT FK_Recepcionista_Empleado
        FOREIGN KEY (legajo)
        REFERENCES Empleado(legajo)
        ON DELETE CASCADE
);



-- Entidad Equipamiento

CREATE TABLE Equipamiento (
    codigoEquipamiento INT NOT NULL,
    idTipoEquipamiento TINYINT NOT NULL,
    idModelo SMALLINT NOT NULL,
    fechaAdquisicion DATE NOT NULL,

    CONSTRAINT PK_Equipamiento
        PRIMARY KEY (codigoEquipamiento),

    CONSTRAINT FK_Equipamiento_TipoEquipamiento
        FOREIGN KEY (idTipoEquipamiento)
        REFERENCES TipoEquipamiento(idTipoEquipamiento),

    CONSTRAINT FK_Equipamiento_Modelo
        FOREIGN KEY (idModelo)
        REFERENCES Modelo(idModelo)
);



-- Entidad Maquina

CREATE TABLE Maquina (
    codigoEquipamiento INT NOT NULL,
    nombre VARCHAR(80) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,

    CONSTRAINT PK_Maquina
        PRIMARY KEY (codigoEquipamiento),

    CONSTRAINT FK_Maquina_Equipamiento
        FOREIGN KEY (codigoEquipamiento)
        REFERENCES Equipamiento(codigoEquipamiento)
        ON DELETE CASCADE
);



-- Entidad BarraDiscoMancuerna

CREATE TABLE BarraDiscoMancuerna (
    codigoEquipamiento INT NOT NULL,
    pesoKg DECIMAL(5,2) NOT NULL,

    CONSTRAINT PK_BarraDiscoMancuerna
        PRIMARY KEY (codigoEquipamiento),

    CONSTRAINT FK_BarraDiscoMancuerna_Equipamiento
        FOREIGN KEY (codigoEquipamiento)
        REFERENCES Equipamiento(codigoEquipamiento)
        ON DELETE CASCADE,

    CONSTRAINT CK_BarraDiscoMancuerna_Peso
        CHECK (pesoKg > 0)
);



-- Entidad Ejercicio

CREATE TABLE Ejercicio (
    codigoEjercicio INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(1000) NOT NULL,
    idGrupoMuscular TINYINT NOT NULL,
    idDificultad TINYINT NOT NULL,
    idTipoEjercicio TINYINT NOT NULL,

    CONSTRAINT PK_Ejercicio
        PRIMARY KEY (codigoEjercicio),

    CONSTRAINT UQ_Ejercicio_Nombre
        UNIQUE (nombre),

    CONSTRAINT FK_Ejercicio_GrupoMuscular
        FOREIGN KEY (idGrupoMuscular)
        REFERENCES GrupoMuscular(idGrupoMuscular),

    CONSTRAINT FK_Ejercicio_Dificultad
        FOREIGN KEY (idDificultad)
        REFERENCES Dificultad(idDificultad),

    CONSTRAINT FK_Ejercicio_TipoEjercicio
        FOREIGN KEY (idTipoEjercicio)
        REFERENCES TipoEjercicio(idTipoEjercicio)
);


-- Ahora voy a armar las entidades transaccionales e históricas

-- Entidad AptoFisico

CREATE TABLE AptoFisico (
    dni CHAR(8) NOT NULL,
    fechaAlta DATE NOT NULL,
    fechaVencimiento DATE NOT NULL,

    CONSTRAINT PK_AptoFisico
        PRIMARY KEY (dni, fechaAlta),

    CONSTRAINT FK_AptoFisico_Socio
        FOREIGN KEY (dni)
        REFERENCES Socio(dni),

    CONSTRAINT CK_AptoFisico_Fechas
        CHECK (fechaVencimiento > fechaAlta)
);



-- Entidad FichadaSocio

CREATE TABLE FichadaSocio (
    dni CHAR(8) NOT NULL,
    fechaHoraIngreso DATETIME2(0) NOT NULL,

    CONSTRAINT PK_FichadaSocio
        PRIMARY KEY (dni, fechaHoraIngreso),

    CONSTRAINT FK_FichadaSocio_Socio
        FOREIGN KEY (dni)
        REFERENCES Socio(dni)
);



-- Entidad Membresia

CREATE TABLE Membresia (
    dni CHAR(8) NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaVencimiento DATE NOT NULL,
    idTipoMembresia TINYINT NOT NULL,
    idMedioPago TINYINT NOT NULL,

    CONSTRAINT PK_Membresia
        PRIMARY KEY (dni, fechaInicio),

    CONSTRAINT FK_Membresia_Socio
        FOREIGN KEY (dni)
        REFERENCES Socio(dni),

    CONSTRAINT FK_Membresia_TipoMembresia
        FOREIGN KEY (idTipoMembresia)
        REFERENCES TipoMembresia(idTipoMembresia),

    CONSTRAINT FK_Membresia_MedioPago
        FOREIGN KEY (idMedioPago)
        REFERENCES MedioPago(idMedioPago),

    CONSTRAINT CK_Membresia_Fechas
        CHECK (fechaVencimiento > fechaInicio)
);



-- Entidad PagoEfectivo

CREATE TABLE PagoEfectivo (
    dni CHAR(8) NOT NULL,
    fechaInicio DATE NOT NULL,
    importeRecibido DECIMAL(10,2) NOT NULL,
    vuelto DECIMAL(10,2) NOT NULL,

    CONSTRAINT PK_PagoEfectivo
        PRIMARY KEY (dni, fechaInicio),

    CONSTRAINT FK_PagoEfectivo_Membresia
        FOREIGN KEY (dni, fechaInicio)
        REFERENCES Membresia(dni, fechaInicio)
        ON DELETE CASCADE,

    CONSTRAINT CK_PagoEfectivo_Importe
        CHECK (importeRecibido >= vuelto)
);



-- Entidad Rutina

CREATE TABLE Rutina (
    dniCliente CHAR(8) NOT NULL,
    fechaCreacion DATE NOT NULL,
    legajo INT NOT NULL,
    idObjetivo TINYINT NOT NULL,
    observaciones VARCHAR(500) NULL,

    CONSTRAINT PK_Rutina
        PRIMARY KEY (dniCliente, fechaCreacion),

    CONSTRAINT FK_Rutina_Socio
        FOREIGN KEY (dniCliente)
        REFERENCES Socio(dni)
        ON DELETE CASCADE,

    CONSTRAINT FK_Rutina_Empleado
        FOREIGN KEY (legajo)
        REFERENCES Empleado(legajo),

    CONSTRAINT FK_Rutina_Objetivo
        FOREIGN KEY (idObjetivo)
        REFERENCES Objetivo(idObjetivo)
);



-- Entidad LiquidacionSueldos

CREATE TABLE LiquidacionSueldos (
    legajo INT NOT NULL,
    fecha DATE NOT NULL,
    monto DECIMAL(10,2) NOT NULL,

    CONSTRAINT PK_LiquidacionSueldos
        PRIMARY KEY (legajo, fecha),

    CONSTRAINT FK_LiquidacionSueldos_Empleado
        FOREIGN KEY (legajo)
        REFERENCES Empleado(legajo)
        ON DELETE CASCADE,

    CONSTRAINT CK_LiquidacionSueldos
        CHECK (monto > 0)
);



-- Entidad FichadaEmpleado

CREATE TABLE FichadaEmpleado (
    legajo INT NOT NULL,
    fechaHora DATETIME2(0) NOT NULL,
    idTipoMovimiento TINYINT NOT NULL,

    CONSTRAINT PK_FichadaEmpleado
        PRIMARY KEY (legajo, fechaHora),

    CONSTRAINT FK_FichadaEmpleado_Empleado
        FOREIGN KEY (legajo)
        REFERENCES Empleado(legajo)
        ON DELETE CASCADE,

    CONSTRAINT FK_FichadaEmpleado_TipoMovimiento
        FOREIGN KEY (idTipoMovimiento)
        REFERENCES TipoMovimiento(idTipoMovimiento)
);



-- Entidad EstadoEmpleado

CREATE TABLE EstadoEmpleado (
    legajo INT NOT NULL,
    fecha DATE NOT NULL,
    idEstadoEmp TINYINT NOT NULL,

    CONSTRAINT PK_EstadoEmpleado
        PRIMARY KEY (legajo, fecha),

    CONSTRAINT FK_EstadoEmpleado_Empleado
        FOREIGN KEY (legajo)
        REFERENCES Empleado(legajo)
        ON DELETE CASCADE,

    CONSTRAINT FK_EstadoEmpleado_EstadoEmpLista
        FOREIGN KEY (idEstadoEmp)
        REFERENCES EstadoEmpLista(idEstadoEmp)
);



-- Entidad LicenciaEmpleado

CREATE TABLE LicenciaEmpleado (
    legajo INT NOT NULL,
    fecha DATE NOT NULL,
    fechaFinLicencia DATE NOT NULL,
    Motivo VARCHAR(50) NOT NULL,

    CONSTRAINT PK_LicenciaEmpleado
        PRIMARY KEY (legajo, fecha),

    CONSTRAINT FK_LicenciaEmpleado_EstadoEmpleado
        FOREIGN KEY (legajo, fecha)
        REFERENCES EstadoEmpleado(legajo, fecha)
        ON DELETE CASCADE,

    CONSTRAINT CK_FechasLicencia
        CHECK (fechaFinLicencia > fecha)
);



-- Entidad SolicitudMantenimiento

CREATE TABLE SolicitudMantenimiento (
    codigoEquipamiento INT NOT NULL,
    fechaSolicitud DATE NOT NULL,
    legajo INT NOT NULL,
    descripcionProblema VARCHAR(500) NOT NULL,

    CONSTRAINT PK_SolicitudMantenimiento
        PRIMARY KEY (codigoEquipamiento, fechaSolicitud),

    CONSTRAINT FK_SolicitudMantenimiento_Equipamiento
        FOREIGN KEY (codigoEquipamiento)
        REFERENCES Equipamiento(codigoEquipamiento),

    CONSTRAINT FK_SolicitudMantenimiento_Empleado
        FOREIGN KEY (legajo)
        REFERENCES Empleado(legajo)
);



-- Entidad MantenimientoHecho

CREATE TABLE MantenimientoHecho (
    codigoEquipamiento INT NOT NULL,
    fechaSolicitud DATE NOT NULL,
    fechaReincorporacion DATE NOT NULL,
    costoReparacion DECIMAL(10,2) NULL,

    CONSTRAINT PK_MantenimientoHecho
        PRIMARY KEY (codigoEquipamiento, fechaSolicitud),

    CONSTRAINT FK_MantenimientoHecho_Solicitud
        FOREIGN KEY (codigoEquipamiento, fechaSolicitud)
        REFERENCES SolicitudMantenimiento(codigoEquipamiento, fechaSolicitud)
        ON DELETE CASCADE,

    CONSTRAINT CK_MantenimientoHecho_Fechas
        CHECK (fechaReincorporacion >= fechaSolicitud),

    CONSTRAINT CK_MantenimientoHecho_Costo
        CHECK (costoReparacion IS NULL OR costoReparacion >= 0)
);



-- Entidad EstadoEquipamiento

CREATE TABLE EstadoEquipamiento (
    codigoEquipamiento INT NOT NULL,
    fechaHoraCambio DATETIME2(0) NOT NULL,
    idEstadoEquipamiento TINYINT NOT NULL,

    CONSTRAINT PK_EstadoEquipamiento
        PRIMARY KEY (codigoEquipamiento, fechaHoraCambio),

    CONSTRAINT FK_EstadoEquipamiento_Equipamiento
        FOREIGN KEY (codigoEquipamiento)
        REFERENCES Equipamiento(codigoEquipamiento)
        ON DELETE CASCADE,

    CONSTRAINT FK_EstadoEquipamiento_EstadoEqLista
        FOREIGN KEY (idEstadoEquipamiento)
        REFERENCES EstadoEqLista(idEstadoEq)
);



-- Entidad DetalleRutina

CREATE TABLE DetalleRutina (
    dniCliente CHAR(8) NOT NULL,
    fechaCreacion DATE NOT NULL,
    orden TINYINT NOT NULL,
    codigoEjercicio INT NOT NULL,
    cantidadSeries TINYINT NOT NULL,
    cantidadRepeticiones TINYINT NOT NULL,
    descansoSegundos SMALLINT NOT NULL,
    observaciones VARCHAR(300) NULL,

    CONSTRAINT PK_DetalleRutina
        PRIMARY KEY (dniCliente, fechaCreacion, orden),

    CONSTRAINT FK_DetalleRutina_Rutina
        FOREIGN KEY (dniCliente, fechaCreacion)
        REFERENCES Rutina(dniCliente, fechaCreacion)
        ON DELETE CASCADE,

    CONSTRAINT FK_DetalleRutina_Ejercicio
        FOREIGN KEY (codigoEjercicio)
        REFERENCES Ejercicio(codigoEjercicio),

    CONSTRAINT CK_DetalleRutina_Orden
        CHECK (orden > 0),

    CONSTRAINT CK_DetalleRutina_CantidadSeries
        CHECK (cantidadSeries > 0),

    CONSTRAINT CK_DetalleRutina_CantidadRepeticiones
        CHECK (cantidadRepeticiones > 0),

    CONSTRAINT CK_DetalleRutina_Descanso
        CHECK (descansoSegundos >= 0)
);



-- Entidad EquipamientoEjercicio

CREATE TABLE EquipamientoEjercicio (
    codigoEjercicio INT NOT NULL,
    idTipoEquipamiento TINYINT NOT NULL,

    CONSTRAINT PK_EquipamientoEjercicio
        PRIMARY KEY (codigoEjercicio, idTipoEquipamiento),

    CONSTRAINT FK_EquipamientoEjercicio_Ejercicio
        FOREIGN KEY (codigoEjercicio)
        REFERENCES Ejercicio(codigoEjercicio)
        ON DELETE CASCADE,

    CONSTRAINT FK_EquipamientoEjercicio_TipoEquipamiento
        FOREIGN KEY (idTipoEquipamiento)
        REFERENCES TipoEquipamiento(idTipoEquipamiento)
);



-- Entidad MaquinaEjercicio

CREATE TABLE MaquinaEjercicio (
    codigoEjercicio INT NOT NULL,
    codigoEquipamiento INT NOT NULL,

    CONSTRAINT PK_MaquinaEjercicio
        PRIMARY KEY (codigoEjercicio, codigoEquipamiento),

    CONSTRAINT FK_MaquinaEjercicio_Ejercicio
        FOREIGN KEY (codigoEjercicio)
        REFERENCES Ejercicio(codigoEjercicio)
        ON DELETE CASCADE,

    CONSTRAINT FK_MaquinaEjercicio_Maquina
        FOREIGN KEY (codigoEquipamiento)
        REFERENCES Maquina(codigoEquipamiento)
        ON DELETE CASCADE
);