
import logging
import os

# Crear la carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar el archivo de registro
logging.basicConfig(
    filename=os.path.join("logs", "eventos.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Registrar eventos exitosos
def registrar_evento(mensaje):
    logging.info(mensaje)


# Registrar errores
def registrar_error(mensaje):
    logging.error(mensaje)

    
# Registrar advertencias
def registrar_advertencia(mensaje):
    logging.warning(mensaje)