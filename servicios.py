
from abc import ABC, abstractmethod


# ==========================================
# CLASE ABSTRACTA SERVICIO
# ==========================================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if (
            not isinstance(tarifa, (int, float))
            or isinstance(tarifa, bool)
            or tarifa <= 0
        ):
            raise ValueError("La tarifa debe ser mayor que cero.")

        self.__nombre = nombre.strip()
        self.__tarifa = tarifa

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tarifa(self):
        return self.__tarifa

    def validar_porcentajes(self, impuesto, descuento):

        for porcentaje, nombre in [
            (impuesto, "El impuesto"),
            (descuento, "El descuento")
        ]:

            if (
                not isinstance(porcentaje, (int, float))
                or isinstance(porcentaje, bool)
                or porcentaje < 0
                or porcentaje > 100
            ):
                raise ValueError(
                    f"{nombre} debe estar entre 0 y 100."
                )

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, cantidad):
        pass


# ==========================================
# SERVICIO DE ALQUILER DE SALA
# ==========================================

class ServicioSala(Servicio):

    def validar_parametros(self, horas):

        if (
            not isinstance(horas, (int, float))
            or isinstance(horas, bool)
            or horas <= 0
        ):
            raise ValueError("Las horas deben ser mayores que cero.")

        return True

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        self.validar_parametros(horas)
        self.validar_porcentajes(impuesto, descuento)

        subtotal = self.tarifa * horas

        return subtotal + subtotal * (impuesto / 100) - subtotal * (descuento / 100)

    def describir_servicio(self):

        return (
            f"Alquiler de sala: {self.nombre}. "
            f"Tarifa por hora: ${self.tarifa:,.0f}"
        )


# ==========================================
# SERVICIO DE ALQUILER DE EQUIPO
# ==========================================

class ServicioEquipo(Servicio):

    def validar_parametros(self, dias):

        if (
            not isinstance(dias, (int, float))
            or isinstance(dias, bool)
            or dias <= 0
        ):
            raise ValueError("Los dias deben ser mayores que cero.")

        return True

    def calcular_costo(self, dias, impuesto=0, descuento=0):

        self.validar_parametros(dias)
        self.validar_porcentajes(impuesto, descuento)

        subtotal = self.tarifa * dias

        return subtotal + subtotal * (impuesto / 100) - subtotal * (descuento / 100)

    def describir_servicio(self):

        return (
            f"Alquiler de equipo: {self.nombre}. "
            f"Tarifa por dia: ${self.tarifa:,.0f}"
        )


# ==========================================
# SERVICIO DE ASESORIA ESPECIALIZADA
# ==========================================

class ServicioAsesoria(Servicio):

    def validar_parametros(self, horas):

        if (
            not isinstance(horas, (int, float))
            or isinstance(horas, bool)
            or horas <= 0
        ):
            raise ValueError("Las horas deben ser mayores que cero.")

        return True

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        self.validar_parametros(horas)
        self.validar_porcentajes(impuesto, descuento)

        subtotal = self.tarifa * horas

        return subtotal + subtotal * (impuesto / 100) - subtotal * (descuento / 100)

    def describir_servicio(self):

        return (
            f"Asesoria especializada: {self.nombre}. "
            f"Tarifa por hora: ${self.tarifa:,.0f}"
        )
