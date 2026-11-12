import logging

logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def registrar_evento(mensaje)
    logging.info(mensaje)

def registrar_error(mensaje):
    logging.error(mensaje)

def registrar_advertencia(mensaje):
    logging.warning(mensaje)
