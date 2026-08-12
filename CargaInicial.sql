use DatosFuertes
GO
/*==========================================================
    IMPORTARCSV - GIMNASIO DATOS FUERTES
==========================================================*/

CREATE OR ALTER PROCEDURE ImportarCSV
    @Tabla NVARCHAR(128),
    @Archivo NVARCHAR(128),
    @Ruta NVARCHAR(260)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @SQL NVARCHAR(MAX);

    SET @SQL = N'
    BULK INSERT ' + QUOTENAME(@Tabla) + '
    FROM ''' + @Ruta + @Archivo + '''
    WITH
    (
        FORMAT = ''CSV'',
        FIRSTROW = 2,
        FIELDTERMINATOR = '','',
        ROWTERMINATOR = ''0x0A'',
        CODEPAGE = ''65001'',
        TABLOCK
    );';

    PRINT 'Importando ' + @Tabla + '...';
    EXEC sp_executesql @SQL;
    PRINT 'Tabla ' + @Tabla + ' importada correctamente.';
END;
GO
DECLARE @RutaCSV NVARCHAR(260);

SET @RutaCSV = N'C:\Users\Mauro\Desktop\Proyectos\datos_fuertes\GeneracionDatos\salida\';

-----------------------------------------------------
-- TABLAS PRINCIPALES
-----------------------------------------------------

EXEC ImportarCSV 'Socio', 'Socio.csv', @RutaCSV;
EXEC ImportarCSV 'Empleado', 'Empleado.csv', @RutaCSV;
EXEC ImportarCSV 'Equipamiento', 'Equipamiento.csv', @RutaCSV;
EXEC ImportarCSV 'Ejercicio', 'Ejercicio.csv', @RutaCSV;

-----------------------------------------------------
-- TRANSACCIONALES
-----------------------------------------------------

EXEC ImportarCSV 'AptoFisico', 'AptoFisico.csv', @RutaCSV;
EXEC ImportarCSV 'Membresia', 'Membresia.csv', @RutaCSV;
EXEC ImportarCSV 'FichadaSocio', 'FichadaSocio.csv', @RutaCSV;
EXEC ImportarCSV 'Rutina', 'Rutina.csv', @RutaCSV;
EXEC ImportarCSV 'SolicitudMantenimiento', 'SolicitudMantenimiento.csv', @RutaCSV;
EXEC ImportarCSV 'FichadaEmpleado', 'FichadaEmpleado.csv', @RutaCSV;
EXEC ImportarCSV 'LiquidacionSueldos', 'LiquidacionSueldos.csv', @RutaCSV;

-----------------------------------------------------
-- ESTADOS
-----------------------------------------------------

EXEC ImportarCSV 'EstadoEquipamiento', 'EstadoEquipamiento.csv', @RutaCSV;
EXEC ImportarCSV 'EstadoEmpleado', 'EstadoEmpleado.csv', @RutaCSV;

-----------------------------------------------------
-- GENERALIZACIONES Y ESPECIALIZACIONES
-----------------------------------------------------

EXEC ImportarCSV 'Maquina', 'Maquina.csv', @RutaCSV;
EXEC ImportarCSV 'BarraDiscoMancuerna', 'BarraDiscoMancuerna.csv', @RutaCSV;
EXEC ImportarCSV 'MantenimientoHecho', 'MantenimientoHecho.csv', @RutaCSV;
EXEC ImportarCSV 'PagoEfectivo', 'PagoEfectivo.csv', @RutaCSV;
EXEC ImportarCSV 'LicenciaEmpleado', 'LicenciaEmpleado.csv', @RutaCSV;
EXEC ImportarCSV 'Recepcionista', 'Recepcionista.csv', @RutaCSV;

-----------------------------------------------------
-- TABLAS INTERMEDIAS
-----------------------------------------------------

EXEC ImportarCSV 'DetalleRutina', 'DetalleRutina.csv', @RutaCSV;

INSERT INTO MaquinaEjercicio (codigoEjercicio, codigoEquipamiento)
VALUES
-- Jalón al pecho
(7,3),
(7,4),
(7,5),

-- Remo sentado
(9,6),
(9,7),

-- Press de pecho
(1,8),
(1,9),

-- Press inclinado
(2,10),

-- Press de hombros
(15,11),

-- Extensión de piernas
(42,12),
(42,13),

-- Curl femoral
(46,14),
(46,15),

-- Abductores
(51,17),

-- Polea alta
(12,18),
(12,19),
(24,18),
(24,19),
(26,18),
(26,19),

-- Polea baja
(50,20),

-- Cruce de poleas
(4,21),

-- Smith
(39,22),
(1,22),
(15,22),

-- Hack squat
(41,23),

-- Pantorrillera
(52,24),
(53,24),

-- Fondos asistidos
(5,25);

INSERT INTO EquipamientoEjercicio (codigoEjercicio, idTipoEquipamiento)
VALUES

-- Pecho
(1,2),(1,4),(1,5),
(2,3),(2,5),
(3,3),(3,5),
(4,1),
(5,1),
(6,6),

-- Espalda
(7,1),
(8,1),
(9,1),
(10,2),(10,4),
(11,3),
(12,1),
(13,2),(13,4),
(14,1),

-- Hombros
(15,2),(15,3),(15,4),
(16,3),
(17,3),
(18,3),
(19,3),

-- Bíceps
(20,2),
(21,3),
(22,3),
(23,1),
(24,1),

-- Tríceps
(25,2),(25,5),
(26,1),
(27,3),
(28,5),
(29,3),

-- Antebrazos
(30,2),
(31,2),
(32,3),(32,7),

-- Abdomen
(33,6),
(34,1),
(35,1),
(36,6),
(37,6),(37,7),
(38,6),

-- Cuádriceps
(39,2),(39,4),
(40,1),
(41,1),
(42,1),
(43,3),
(44,3),(44,5),

-- Isquiotibiales
(45,2),(45,4),
(46,1),
(47,2),(47,4),

-- Glúteos
(48,6),
(49,1),(49,2),(49,4),(49,5),
(50,1),
(51,1),

-- Gemelos
(52,1),
(53,1),

-- Movilidad y flexibilidad
(54,8),
(55,6);