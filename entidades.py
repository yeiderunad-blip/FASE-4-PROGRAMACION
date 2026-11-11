
from abc import ABC, abstractmethod


# Clase abstracta que representa una entidad del sistema
class Entidad(ABC):

    def __init__(self, identificacion):
        self._identificacion = identificacion

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        # Validar los datos del cliente
        if not identificacion or not identificacion.strip():
            raise ValueError("La identificación es obligatoria.")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        if "@" not in correo:
            raise ValueError("El correo no es válido.")

        if not telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números.")

        # Atributos privados del cliente
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def mostrar_informacion(self):

        return (
            f"Identificación: {self._identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
