from entidades import Entidad

# La clase Servicio hereda de la clase abstracta Entidad
class Servicio(Entidad):
    def __init__(self, identificacion, nombre, precio):
      
        # Llama al constructor de la clase madre (Entidad)
        super().__init__(identificacion)
        
        # Validacion básica
        if not identificacion or not str(identificacion).strip():
            raise ValueError("La identificación del servicio es obligatoria.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")
        if precio <= 0:
            raise ValueError("El precio del servicio debe ser mayor a cero.")

        # Atributos privados
        self.__nombre = nombre
        self.__precio = precio

    # Métodos para obtener información (getters)
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    # Método obligatorio heredado de Entidad
    def mostrar_informacion(self):
        return (
            f"ID Servicio: {self._identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Precio: ${self.__precio:,.2f}"
        )
