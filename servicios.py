
from abc import ABC, abstractmethod


# ==========================================
# CLASE ABSTRACTA SERVICIO
# ==========================================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor que cero.")

        self.__nombre = nombre.strip()
        self.__tarifa = tarifa

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tarifa(self):
        return self.__tarifa

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass


# ==========================================
# SERVICIO DE ALQUILER DE SALAS
# ==========================================

class ServicioSala(Servicio):

    def calcular_costo(self, horas):

        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        return self.tarifa * horas


# ==========================================
# SERVICIO DE ALQUILER DE EQUIPOS
# ==========================================

class ServicioEquipo(Servicio):

    def calcular_costo(self, dias):

        if not isinstance(dias, (int, float)) or dias <= 0:
            raise ValueError("Los dias deben ser mayores que cero.")

        return self.tarifa * dias


# ==========================================
# SERVICIO DE ASESORIAS
# ==========================================

class ServicioAsesoria(Servicio):

    def calcular_costo(self, horas):

        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        return self.tarifa * horas
