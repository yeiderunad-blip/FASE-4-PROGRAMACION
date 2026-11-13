from excepciones import ReservaInvalidaError

from entidades import Cliente
from servicios import ServicioSala
from reservas import Reserva

# Crear cliente y servicio para la prueba
cliente = Cliente(
    "123456",
    "Cliente de prueba",
    "prueba@gmail.com",
    "3001234567"
)

servicio = ServicioSala("Alquiler de sala", 30000)

# Crear reserva
reserva = Reserva(cliente, servicio, 2)

print("ESTADO INICIAL:")
print(reserva.mostrar_reserva())

# Confirmar reserva
reserva.confirmar()
print("\nDESPUES DE CONFIRMAR:")
print("Estado:", reserva.estado)

# Procesar reserva
reserva.procesar()
print("\nDESPUES DE PROCESAR:")
print("Estado:", reserva.estado)

print("\nPRUEBA FINALIZADA CORRECTAMENTE.")

# Crear otra reserva para probar la cancelacion
reserva_cancelacion = Reserva(cliente, servicio, 1)

print("\nPRUEBA DE CANCELACION:")
reserva_cancelacion.cancelar()

print("Estado:", reserva_cancelacion.estado)

# Probar una operacion no permitida
print("\nPRUEBA DE ERROR CONTROLADO:")

try:
    reserva.cancelar()

except ReservaInvalidaError as error:
    print("Error controlado:", error)