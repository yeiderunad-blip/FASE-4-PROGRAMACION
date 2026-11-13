
from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError


# ==========================================
# CLASE ABSTRACTA ENTIDAD
# ==========================================

class Entidad(ABC):

    def __init__(self, identificacion):

        if not isinstance(identificacion, str):
            raise ValueError("La identificacion debe ser texto.")

        if not identificacion.strip():
            raise ValueError("La identificacion es obligatoria.")

        self.__identificacion = identificacion.strip()

    @property
    def identificacion(self):
        return self.__identificacion

    @abstractmethod
    def mostrar_informacion(self):
        pass


# ==========================================
# CLASE CLIENTE
# ==========================================

class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        # Validar identificacion
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ClienteInvalidoError(
                "La identificacion es obligatoria y debe ser texto."
            )

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ClienteInvalidoError("El nombre es obligatorio.")

        # Validar correo
        if not isinstance(correo, str):
            raise ClienteInvalidoError("El correo debe ser texto.")

        correo = correo.strip()

        if "@" not in correo or "." not in correo.split("@")[-1]:
            raise ClienteInvalidoError(
                "El correo electronico no es valido."
            )

        # Validar telefono
        if not isinstance(telefono, str) or not telefono.isdigit():
            raise ClienteInvalidoError(
                "El telefono debe contener solamente numeros."
            )

        # Inicializar la clase padre
        super().__init__(identificacion)

        # Atributos privados del cliente
        self.__nombre = nombre.strip()
        self.__correo = correo
        self.__telefono = telefono

    # Metodo para mostrar la informacion del cliente
    def mostrar_informacion(self):

        return (
            f"Identificacion: {self.identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )

