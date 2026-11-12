
from entidades import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reservas import Reserva


# Listas para almacenar la informacion durante la ejecucion
clientes = []
reservas = []


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

        clientes.append(cliente)

        print("\nCliente registrado correctamente.")

    except ValueError as error:
        print(f"\nError: {error}")


def consultar_clientes():
    print("\n--- LISTA DE CLIENTES ---")

    if not clientes:
        print("No hay clientes registrados.")
        return

    for numero, cliente in enumerate(clientes, start=1):
        print(f"\nCliente numero {numero}")
        print(cliente.mostrar_informacion())


def registrar_reserva():
    print("\n--- REGISTRO DE RESERVA ---")

    if not clientes:
        print("Primero debe registrar un cliente.")
        return

    print("\nSeleccione un cliente:")

    for numero, cliente in enumerate(clientes, start=1):
        print(f"{numero}. {cliente.mostrar_informacion()}")

    try:
        opcion_cliente = int(input("\nNumero del cliente: "))

        if opcion_cliente < 1 or opcion_cliente > len(clientes):
            print("Seleccion de cliente no valida.")
            return

        cliente = clientes[opcion_cliente - 1]

        print("\nSeleccione el servicio:")
        print("1. Alquiler de sala - $30.000")
        print("2. Alquiler de equipo - $20.000")
        print("3. Asesoria - $40.000")

        opcion_servicio = int(input("Opcion: "))

        if opcion_servicio == 1:
            servicio = ServicioSala("Alquiler de sala", 30000)

        elif opcion_servicio == 2:
            servicio = ServicioEquipo("Alquiler de equipo", 20000)

        elif opcion_servicio == 3:
            servicio = ServicioAsesoria("Asesoria", 40000)

        else:
            print("Servicio no valido.")
            return

        cantidad = int(input("Ingrese la cantidad de horas o unidades: "))

        reserva = Reserva(cliente, servicio, cantidad)

        reservas.append(reserva)

        print("\n¡RESERVA REGISTRADA!")
        print(reserva.mostrar_reserva())

    except ValueError as error:
        print(f"\nError: {error}")


def consultar_reservas():
    print("\n--- RESERVAS REGISTRADAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for numero, reserva in enumerate(reservas, start=1):
        print(f"\nReserva numero {numero}")
        print(reserva.mostrar_reserva())


# PROGRAMA PRINCIPAL

def iniciar_programa():

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
            break

        else:
            print("\nOpcion incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    iniciar_programa()
