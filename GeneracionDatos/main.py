from generadores.generador_personas import GeneradorPersonas
from generadores.generador_socios import GeneradorSocios
from generadores.generador_aptos_fisicos import GeneradorAptosFisicos
from generadores.generador_membresias import GeneradorMembresias
from generadores.generador_pago_efectivo import GeneradorPagoEfectivo
from generadores.generador_fichadas_socios import GeneradorFichadasSocios
from generadores.generador_empleados import GeneradorEmpleados
from generadores.generador_estado_empleado import GeneradorEstadosEmpleado
from generadores.generador_licencia_empleado import GeneradorLicenciasEmpleado
from generadores.generador_recepcionista import GeneradorRecepcionistas
from generadores.generador_fichadas_empleado import GeneradorFichadasEmpleado
from generadores.generador_liquidacion_sueldos import GeneradorLiquidacionesSueldos
from generadores.generador_rutina import GeneradorRutinas
from generadores.generador_equipamiento import GeneradorEquipamiento
from generadores.generador_barra_disco_mancuerna import GeneradorBarraDiscoMancuerna
from generadores.generador_maquina import GeneradorMaquinas
from generadores.generador_solicitud_mantenimiento import GeneradorSolicitudMantenimiento
from generadores.generador_mantenimiento_hecho import GeneradorMantenimientoHecho
from generadores.generador_estado_equipamiento import GeneradorEstadoEquipamiento
from generadores.generador_ejercicio import GeneradorEjercicio
from generadores.generador_detalle_rutina import GeneradorDetalleRutina

from utilidades.exportador import ExportadorCSV

from tipos_sql import (
    TIPOS_SOCIO,
    TIPOS_APTO_FISICO,
    TIPOS_MEMBRESIA,
    TIPOS_PAGO_EFECTIVO,
    TIPOS_FICHADA_SOCIO,
    TIPOS_EMPLEADO,
    TIPOS_ESTADO_EMPLEADO,
    TIPOS_LICENCIA_EMPLEADO,
    TIPOS_RECEPCIONISTA,
    TIPOS_FICHADA_EMPLEADO,
    TIPOS_LIQUIDACION_SUELDOS,
    TIPOS_RUTINA,
    TIPOS_EQUIPAMIENTO,
    TIPOS_BARRA_DISCO_MANCUERNA,
    TIPOS_MAQUINA,
    TIPOS_SOLICITUD_MANTENIMIENTO,
    TIPOS_MANTENIMIENTO_HECHO,
    TIPOS_ESTADO_EQUIPAMIENTO,
    TIPOS_EJERCICIO,
    TIPOS_DETALLE_RUTINA
)


def main():

    # Generadores
    generador_personas = GeneradorPersonas()
    generador_socios = GeneradorSocios(generador_personas)
    generador_aptos = GeneradorAptosFisicos()
    generador_membresias = GeneradorMembresias()
    generador_pagosefectivo = GeneradorPagoEfectivo()
    generador_fichadassocio = GeneradorFichadasSocios()
    generador_empleados = GeneradorEmpleados(generador_personas)
    generador_estadosempleado = GeneradorEstadosEmpleado()
    generador_licencias = GeneradorLicenciasEmpleado()
    generador_recepcionistas = GeneradorRecepcionistas()
    generador_fichadasempleado = GeneradorFichadasEmpleado()
    generador_liquidacionsueldos = GeneradorLiquidacionesSueldos()
    generador_rutina = GeneradorRutinas()
    generador_equipamiento = GeneradorEquipamiento()
    generador_barradiscomancuerna = GeneradorBarraDiscoMancuerna()
    generador_maquina = GeneradorMaquinas()
    generador_solicitudmantenimiento = GeneradorSolicitudMantenimiento()
    generador_mantenimiento = GeneradorMantenimientoHecho()
    generador_estadosequipamiento = GeneradorEstadoEquipamiento()
    generador_ejercicio = GeneradorEjercicio()
    generador_detalle_rutina = GeneradorDetalleRutina()

    # Generación de datos
    socios = generador_socios.generar(200)
    aptos = generador_aptos.generar(socios)
    membresias = generador_membresias.generar(socios)
    pagosefectivo = generador_pagosefectivo.generar(membresias)
    fichadassocio = generador_fichadassocio.generar(membresias,aptos)
    empleados = generador_empleados.generar()
    estadosempleado = generador_estadosempleado.generar(empleados)
    licencias = generador_licencias.generar(estadosempleado)
    recepcionistas = generador_recepcionistas.generar(empleados, estadosempleado)
    fichadasempleado = generador_fichadasempleado.generar(empleados, estadosempleado)
    liquidacionsueldos = generador_liquidacionsueldos.generar(empleados, estadosempleado)
    rutinas = generador_rutina.generar(socios, empleados, estadosempleado, membresias)
    equipamiento = generador_equipamiento.generar()
    barradiscomancuerna = generador_barradiscomancuerna.generar(equipamiento)
    maquina = generador_maquina.generar(equipamiento)
    solicitudmantenimiento = generador_solicitudmantenimiento.generar(equipamiento, empleados, estadosempleado)
    mantenimiento = generador_mantenimiento.generar(solicitudmantenimiento)
    estadosequipamiento = generador_estadosequipamiento.generar(equipamiento, solicitudmantenimiento, mantenimiento)
    ejercicios = generador_ejercicio.generar()
    detallerutina = generador_detalle_rutina.generar(rutinas, ejercicios)

    # Exportación
    exportador = ExportadorCSV()

    exportador.exportar(
        socios,
        "Socio",
        TIPOS_SOCIO
    )

    exportador.exportar(
        aptos,
        "AptoFisico",
        TIPOS_APTO_FISICO
    )

    exportador.exportar(
        membresias,
        "Membresia",
        TIPOS_MEMBRESIA
    )

    exportador.exportar(
        pagosefectivo,
        "PagoEfectivo",
        TIPOS_PAGO_EFECTIVO
    )

    exportador.exportar(
        fichadassocio,
        "FichadaSocio",
        TIPOS_FICHADA_SOCIO
    )

    exportador.exportar(
        empleados,
        "Empleado",
        TIPOS_EMPLEADO
    )

    exportador.exportar(
        estadosempleado,
        "EstadoEmpleado",
        TIPOS_ESTADO_EMPLEADO
        )

    exportador.exportar(
        licencias,
        "LicenciaEmpleado",
        TIPOS_LICENCIA_EMPLEADO
        )

    exportador.exportar(
        recepcionistas,
        "Recepcionista",
        TIPOS_RECEPCIONISTA
        )

    exportador.exportar(
        fichadasempleado,
        "FichadaEmpleado",
        TIPOS_FICHADA_EMPLEADO
        )

    exportador.exportar(
        liquidacionsueldos,
        "LiquidacionSueldos",
        TIPOS_LIQUIDACION_SUELDOS
        )

    exportador.exportar(
        rutinas,
        "Rutina",
        TIPOS_RUTINA
        )

    exportador.exportar(
        equipamiento,
        "Equipamiento",
        TIPOS_EQUIPAMIENTO
        )

    exportador.exportar(
        barradiscomancuerna,
        "BarraDiscoMancuerna",
        TIPOS_BARRA_DISCO_MANCUERNA
        )

    exportador.exportar(
        maquina,
        "Maquina",
        TIPOS_MAQUINA
        )

    exportador.exportar(
        solicitudmantenimiento,
        "SolicitudMantenimiento",
        TIPOS_SOLICITUD_MANTENIMIENTO
        )

    exportador.exportar(
        mantenimiento,
        "MantenimientoHecho",
        TIPOS_MANTENIMIENTO_HECHO
        )

    exportador.exportar(
        estadosequipamiento,
        "EstadoEquipamiento",
        TIPOS_ESTADO_EQUIPAMIENTO
        )

    exportador.exportar(
        ejercicios,
        "Ejercicio",
        TIPOS_EJERCICIO
    )

    exportador.exportar(
        detallerutina,
        "DetalleRutina",
        TIPOS_DETALLE_RUTINA
        )

if __name__ == "__main__":
    main()