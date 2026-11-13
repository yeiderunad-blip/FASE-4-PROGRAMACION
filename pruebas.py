
from entidades import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reservas import Reserva

from excepciones import (
    ClienteInvalidoError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError
)

from logs import registrar_evento, registrar_error


# ==========================================
# FUNCION PARA EJECUTAR Y CONTROLAR PRUEBAS
# ==========================================

total_pruebas = 0
pruebas_correctas = 0


def ejecutar_prueba(nombre, accion, excepcion_esperada=None):

    global total_pruebas, pruebas_correctas

    total_pruebas += 1

    print(f"\nPRUEBA {total_pruebas}: {nombre}")

    resultado = None

    try:
        resultado = accion()

    except Exception as error:

        if (
            excepcion_esperada is not None
            and isinstance(error, excepcion_esperada)
        ):

            print(f"CORRECTO: Error controlado: {error}")

            registrar_evento(
                f"Prueba superada: {nombre}. Error esperado: {error}"
            )

            pruebas_correctas += 1

        else:

            print(f"ERROR INESPERADO: {error}")

            registrar_error(
                f"Fallo en prueba: {nombre}. Detalle: {error}"
            )

    else:

        if excepcion_esperada is not None:

            print("ERROR: No se produjo la excepcion esperada.")

            registrar_error(
                f"Fallo en prueba: {nombre}. "
                "No se produjo el error esperado."
            )

        else:

            print("CORRECTO: Operacion realizada.")

            registrar_evento(
                f"Prueba superada: {nombre}"
            )

            pruebas_correctas += 1

    return resultado




# ==========================================
# INICIO DE LAS PRUEBAS
# ==========================================

print("\n==========================================")
print("       SOFTWARE FJ - PRUEBAS")
print("==========================================")

registrar_evento("Inicio de las pruebas generales de Software FJ.")


# ==========================================
# 1. REGISTRO DE CLIENTE VALIDO
# ==========================================

cliente = ejecutar_prueba(
    "Registro de cliente valido",
    lambda: Cliente(
        "123456",
        "Cliente de prueba",
        "prueba@gmail.com",
        "3001234567"
    )
)


# ==========================================
# 2. REGISTRO DE CLIENTE INVALIDO
# ==========================================

ejecutar_prueba(
    "Registro de cliente con correo invalido",
    lambda: Cliente(
        "654321",
        "Cliente invalido",
        "correo_incorrecto",
        "3001234567"
    ),
    ClienteInvalidoError
)


# ==========================================
# 3. CREACION DE SERVICIO DE SALA
# ==========================================

sala = ejecutar_prueba(
    "Creacion de servicio de sala",
    lambda: ServicioSala("Sala principal", 30000)
)


# ==========================================
# 4. CREACION DE SERVICIO DE EQUIPO
# ==========================================

equipo = ejecutar_prueba(
    "Creacion de servicio de equipo",
    lambda: ServicioEquipo("Computador", 20000)
)


# ==========================================
# 5. CREACION DE SERVICIO DE ASESORIA
# ==========================================

asesoria = ejecutar_prueba(
    "Creacion de servicio de asesoria",
    lambda: ServicioAsesoria("Asesoria tecnica", 40000)
)


# ==========================================
# 6. CREACION DE SERVICIO INVALIDO
# ==========================================

ejecutar_prueba(
    "Creacion de servicio con tarifa invalida",
    lambda: ServicioSala("Sala invalida", -100),
    ValueError
)


# ==========================================
# 7. CREACION DE RESERVA VALIDA
# ==========================================

reserva = ejecutar_prueba(
    "Creacion de reserva valida",
    lambda: Reserva(cliente, sala, 2)
)


# ==========================================
# 8. RESERVA CON CLIENTE INVALIDO
# ==========================================

ejecutar_prueba(
    "Reserva con cliente no valido",
    lambda: Reserva("Cliente incorrecto", sala, 2),
    ClienteNoEncontradoError
)


# ==========================================
# 9. RESERVA CON SERVICIO INVALIDO
# ==========================================

ejecutar_prueba(
    "Reserva con servicio no valido",
    lambda: Reserva(cliente, "Servicio incorrecto", 2),
    ServicioNoDisponibleError
)


# ==========================================
# 10. RESERVA CON CANTIDAD INVALIDA
# ==========================================

ejecutar_prueba(
    "Reserva con cantidad incorrecta",
    lambda: Reserva(cliente, sala, 0),
    ReservaInvalidaError
)


# ==========================================
# 11. CONFIRMACION DE RESERVA
# ==========================================

ejecutar_prueba(
    "Confirmacion de reserva",
    lambda: reserva.confirmar()
)


# ==========================================
# 12. PROCESAMIENTO DE RESERVA
# ==========================================

ejecutar_prueba(
    "Procesamiento de reserva",
    lambda: reserva.procesar()
)


# ==========================================
# 13. CANCELACION DE RESERVA
# ==========================================

reserva_cancelacion = Reserva(cliente, equipo, 2)

ejecutar_prueba(
    "Cancelacion de reserva pendiente",
    lambda: reserva_cancelacion.cancelar()
)


# ==========================================
# 14. OPERACION NO PERMITIDA
# ==========================================

ejecutar_prueba(
    "Cancelacion de reserva procesada",
    lambda: reserva.cancelar(),
    ReservaInvalidaError
)


# ==========================================
# RESUMEN FINAL
# ==========================================

print("\n==========================================")
print("          RESULTADOS FINALES")
print("==========================================")

print(f"Total de pruebas: {total_pruebas}")
print(f"Pruebas correctas: {pruebas_correctas}")
print(f"Pruebas fallidas: {total_pruebas - pruebas_correctas}")

if pruebas_correctas == total_pruebas:
    print("\nTODAS LAS PRUEBAS FUERON SUPERADAS.")
    registrar_evento("Todas las pruebas generales fueron superadas.")
else:
    print("\nHAY PRUEBAS QUE NECESITAN REVISION.")
    registrar_error("Una o mas pruebas generales no fueron superadas.")

print("\nFIN DE LAS PRUEBAS DE SOFTWARE FJ.")
