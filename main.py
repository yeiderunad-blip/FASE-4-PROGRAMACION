
from entidades import Cliente

# Crear un cliente de prueba
cliente1 = Cliente(
    "123456",
    "Carlos Perez",
    "carlos@gmail.com",
    "3001234567"
)

# Mostrar información
print("CLIENTE REGISTRADO")
print(cliente1.mostrar_informacion())
