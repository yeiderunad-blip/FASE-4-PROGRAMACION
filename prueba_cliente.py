
from entidades import Cliente
from excepciones import ClienteInvalidoError

print("PRUEBA DE VALIDACION DE CLIENTES")

try:
    cliente = Cliente(
        "12345",
        "Cliente Prueba",
        "correo-invalido",
        "3001234567"
    )

    print(cliente.mostrar_informacion())

except ClienteInvalidoError as error:
    print("Error controlado:", error)

print("PRUEBA FINALIZADA.")
