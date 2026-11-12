
# ==========================================
# MANEJO DE EXCEPCIONES - SOFTWARE FJ
# ==========================================


# Excepcion general del sistema
class ErrorSoftwareFJ(Exception):
    pass


# Error cuando un cliente no es valido
class ClienteNoEncontradoError(ErrorSoftwareFJ):
    pass


# Error cuando un servicio no esta disponible
class ServicioNoDisponibleError(ErrorSoftwareFJ):
    pass


# Error cuando una reserva tiene datos incorrectos
class ReservaInvalidaError(ErrorSoftwareFJ):
    pass
