TIPOS_SOCIO = {
    "dni": "int",
    "numeroDomicilio": "int",
    "pisoDomicilio": "Int64",
    "fechaNacimiento": "datetime64[ns]",
    "fechaAlta": "datetime64[ns]"
}

TIPOS_APTO_FISICO = {
    "dni_socio": "int",
    "fecha_presentacion": "datetime64[ns]",
    "fecha_vencimiento": "datetime64[ns]"
}

TIPOS_MEMBRESIA = {
    "dni_socio": "int",
    "fecha_inicio": "datetime64[ns]",
    "fecha_fin": "datetime64[ns]",
    "id_tipo_membresia": "int",
    "id_medio_pago": "int"
}

TIPOS_PAGO_EFECTIVO = {
    "dni": "string",
    "fechaInicio": "datetime64[ns]",
    "importeRecibido": "float",
    "vuelto": "float"
}

TIPOS_FICHADA_SOCIO = {
    "dni": "string",
    "fechaHora": "datetime64[ns]"
}

TIPOS_EMPLEADO = {
    "legajo" : "int",
    "dni": "string",
    "nombre": "string",
    "apellido": "string",
    "fechaNacimiento": "datetime64[ns]",
    "telefono": "string",
    "correoElectronico": "string",
    "direccionDomicilio": "string",
    "numeroDomicilio": "int",
    "pisoDomicilio": "Int64",
    "codigoPostalDomicilio": "string",
    "fechaIngreso": "datetime64[ns]",
    "idCargo": "int",
    "idTurno": "int"
}

TIPOS_ESTADO_EMPLEADO = {
    "legajo": "int",
    "fecha": "datetime64[ns]",
    "idEstadoEmp": "int"
}

TIPOS_LICENCIA_EMPLEADO = {
    "legajo": "int",
    "fecha": "datetime64[ns]",
    "fechaFinLicencia": "datetime64[ns]",
    "motivo": "string"
}

TIPOS_RECEPCIONISTA = {
    "legajo": "int",
    "telCorpAsig": "string"
}

TIPOS_FICHADA_EMPLEADO = {
    "legajo": "int",
    "fechaHora": "datetime64[ns]",
    "idTipoMovimiento": "int"
}

TIPOS_LIQUIDACION_SUELDOS = {
    "legajo": "int",
    "fecha": "datetime64[ns]",
    "monto": "float"
}

TIPOS_RUTINA = {
    "dniCliente": "int",
    "fechaCreacion": "datetime64[ns]",
    "legajo": "int",
    "idObjetivo": "int",
    "observaciones": "string"
}

TIPOS_EQUIPAMIENTO = {
    "codigoEquipamiento": "int",
    "idTipoEquipamiento": "int",
    "idModelo": "int",
    "fechaAdquisicion": "datetime64[ns]"
}

TIPOS_BARRA_DISCO_MANCUERNA = {
    "codigoEquipamiento": "int",
    "pesoKg": "float"
}

TIPOS_MAQUINA = {
    "codigoEquipamiento": "int",
    "nombre": "string",
    "descripcion": "string"
}

TIPOS_SOLICITUD_MANTENIMIENTO = {
    "codigoEquipamiento": "int",
    "fechaSolicitud": "datetime64[ns]",
    "legajo": "int",
    "descripcionProblema": "string"
}

TIPOS_MANTENIMIENTO_HECHO = {
    "codigoEquipamiento": "int",
    "fechaSolicitud": "datetime64[ns]",
    "fechaReincorporacion": "datetime64[ns]",
    "costoReparacion": "float"
}

TIPOS_ESTADO_EQUIPAMIENTO = {
    "codigoEquipamiento": "int",
    "fechaHoraCambio": "datetime64[ns]",
    "idEstadoEquipamiento": "int"
}

TIPOS_EJERCICIO = {
    "codigoEjercicio": "int",
    "nombre": "string",
    "descripcion": "string",
    "idGrupoMuscular": "int",
    "idDificultad": "int",
    "idTipoEjercicio": "int"
}

TIPOS_DETALLE_RUTINA = {
    "dniCliente": "string",
    "fechaCreacion": "datetime64[ns]",
    "orden": "int",
    "codigoEjercicio": "int",
    "cantidadSeries": "int",
    "cantidadRepeticiones": "int",
    "descansoSegundos": "int",
    "observaciones": "string"
}