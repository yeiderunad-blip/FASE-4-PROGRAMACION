
from entidades import Cliente
from servicios import Servicio
from excepciones import (
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError
)

# ==========================================
# CLASE RESERVA
# ==========================================

class Reserva:

    def __init__(self, cliente, servicio, cantidad):

        # Validar cliente
        if not isinstance(cliente, Cliente):
            raise ClienteNoEncontradoError("El cliente no es válido.")

        # Validar servicio
        if not isinstance(servicio, Servicio):
            raise ServicioNoDisponibleError("El servicio no es válido.")

        # Validar cantidad
        if (not isinstance(cantidad, (int, float))
        or isinstance(cantidad, bool)
        or cantidad <= 0):
           raise ReservaInvalidaError("La cantidad debe ser mayor que cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad

    # Calcular el costo de la reserva
    def calcular_total(self):
        return self.servicio.calcular_costo(self.cantidad)

    # Mostrar informacion de la reserva
    def mostrar_reserva(self):

        return (
            "========== RESERVA ==========\n"
            f"{self.cliente.mostrar_informacion()}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Cantidad: {self.cantidad}\n"
            f"Total a pagar: ${self.calcular_total():,.0f}"
        )
