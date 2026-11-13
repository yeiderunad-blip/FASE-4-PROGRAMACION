
from entidades import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reservas import Reserva

from excepciones import (
    ClienteInvalidoError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError
)

from logs import (
    registrar_evento,
    registrar_error,
    registrar_advertencia
)


# ==========================================
# LISTAS DEL SISTEMA
# ==========================================

clientes = []
reservas = []


# ==========================================
# MOSTRAR MENU PRINCIPAL
# ==========================================

def mostrar_menu():

    print("\n================================")
    print("          SOFTWARE FJ")
    print("================================")
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Registrar reserva")
    print("4. Consultar reservas")
    print("5. Salir")
    print("================================")


# ==========================================
# REGISTRAR CLIENTE
# ==========================================

def registrar_cliente():

    print("\n--- REGISTRO DE CLIENTE ---")

    try:
        identificacion = input("Identificacion: ")
        nombre = input("Nombre completo: ")
        correo = input("Correo electronico: ")
        telefono = input("Telefono: ")

        cliente = Cliente(
            identificacion,
            nombre,
            correo,
            telefono
        )

    except ClienteInvalidoError as error:

        registrar_error(
            f"Error al registrar cliente: {error}"
        )

        print(f"\nError: {error}")

    except ValueError as error:

        registrar_error(
            f"Error de datos del cliente: {error}"
        )

        print(f"\nError: {error}")

    else:

        clientes.append(cliente)

        registrar_evento(
            f"Cliente registrado: {identificacion}"
        )

        print("\nCliente registrado correctamente.")


# ==========================================
# CONSULTAR CLIENTES
# ==========================================

def consultar_clientes():

    print("\n--- LISTA DE CLIENTES ---")

    if not clientes:
        print("No hay clientes registrados.")
        return

    for numero, cliente in enumerate(clientes, start=1):

        print(f"\nCliente numero {numero}")
        print(cliente.mostrar_informacion())


# ==========================================
# LEER CANTIDAD Y VALIDAR DATOS
# ==========================================

def leer_cantidad():
    

    try:
        cantidad = int(
            input("Ingrese la cantidad de horas o unidades: ")
        )

    except ValueError as error:

        raise ReservaInvalidaError(
            "La cantidad debe ser un numero entero."
        ) from error

    return cantidad


# ==========================================
# REGISTRAR RESERVA
# ==========================================

def registrar_reserva():

    print("\n--- REGISTRO DE RESERVA ---")

    try:

        if not clientes:
            print("Primero debe registrar un cliente.")
            return

        print("\nSeleccione un cliente:")

        for numero, cliente in enumerate(clientes, start=1):
            print(f"{numero}. {cliente.mostrar_informacion()}")

        opcion_cliente = int(
            input("\nNumero del cliente: ")
        )

        if opcion_cliente < 1 or opcion_cliente > len(clientes):

            raise ClienteNoEncontradoError(
                "El cliente seleccionado no existe."
            )

        cliente = clientes[opcion_cliente - 1]

        print("\nSeleccione el servicio:")
        print("1. Alquiler de sala - $30.000")
        print("2. Alquiler de equipo - $20.000")
        print("3. Asesoria - $40.000")

        opcion_servicio = int(input("Opcion: "))

        if opcion_servicio == 1:

            servicio = ServicioSala(
                "Alquiler de sala", 30000
            )

        elif opcion_servicio == 2:

            servicio = ServicioEquipo(
                "Alquiler de equipo", 20000
            )

        elif opcion_servicio == 3:

            servicio = ServicioAsesoria(
                "Asesoria", 40000
            )

        else:

            raise ServicioNoDisponibleError(
                "El servicio seleccionado no existe."
            )

        cantidad = leer_cantidad()

        reserva = Reserva(
            cliente,
            servicio,
            cantidad
        )

    except (
        ValueError,
        ClienteNoEncontradoError,
        ServicioNoDisponibleError,
        ReservaInvalidaError
    ) as error:

        registrar_error(
            f"Error al registrar reserva: {error}"
        )

        print(f"\nError: {error}")

    else:

        reservas.append(reserva)

        registrar_evento(
            f"Reserva registrada para el cliente: "
            f"{cliente.identificacion}"
        )

        print("\n¡RESERVA REGISTRADA!")
        print(reserva.mostrar_reserva())

    finally:

        registrar_evento(
            "Finalizo el intento de registro de reserva."
        )


# ==========================================
# CONSULTAR RESERVAS
# ==========================================

def consultar_reservas():

    print("\n--- RESERVAS REGISTRADAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for numero, reserva in enumerate(reservas, start=1):

        print(f"\nReserva numero {numero}")
        print(reserva.mostrar_reserva())


# ==========================================
# INICIAR PROGRAMA
# ==========================================

def iniciar_programa():

    registrar_evento(
        "El programa Software FJ ha iniciado."
    )

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            registrar_cliente()

        elif opcion == "2":

            consultar_clientes()

        elif opcion == "3":

            registrar_reserva()

        elif opcion == "4":

            consultar_reservas()

        elif opcion == "5":

            print("\nGracias por utilizar SOFTWARE FJ.")
            print("Programa finalizado.")

            registrar_evento(
                "El programa Software FJ ha finalizado."
            )

            break

        else:

            registrar_advertencia(
                f"Opcion incorrecta seleccionada: {opcion}"
            )

            print("\nOpcion incorrecta. Intente nuevamente.")


# ==========================================
# EJECUTAR PROGRAMA
# ==========================================

if __name__ == "__main__":
    iniciar_programa()
