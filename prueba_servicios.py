
from servicios import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)

# ==========================================
# PRUEBA 1: SERVICIO DE SALA
# ==========================================

print("\n========== SERVICIO DE SALA ==========")

sala = ServicioSala("Sala principal", 30000)

print(sala.describir_servicio())
print("Costo normal:", sala.calcular_costo(2))
print("Con impuesto:", sala.calcular_costo(2, 19))
print("Con impuesto y descuento:", sala.calcular_costo(2, 19, 10))


# ==========================================
# PRUEBA 2: SERVICIO DE EQUIPO
# ==========================================

print("\n========== SERVICIO DE EQUIPO ==========")

equipo = ServicioEquipo("Computador", 20000)

print(equipo.describir_servicio())
print("Costo normal:", equipo.calcular_costo(3))
print("Con impuesto:", equipo.calcular_costo(3, 19))
print("Con impuesto y descuento:", equipo.calcular_costo(3, 19, 10))


# ==========================================
# PRUEBA 3: SERVICIO DE ASESORIA
# ==========================================

print("\n========== SERVICIO DE ASESORIA ==========")

asesoria = ServicioAsesoria("Asesoria tecnica", 40000)

print(asesoria.describir_servicio())
print("Costo normal:", asesoria.calcular_costo(2))
print("Con impuesto:", asesoria.calcular_costo(2, 19))
print("Con impuesto y descuento:", asesoria.calcular_costo(2, 19, 10))


# ==========================================
# PRUEBA 4: VALIDACION DE PORCENTAJES
# ==========================================

print("\n========== PRUEBA DE VALIDACION ==========")

try:
    sala.calcular_costo(2, 150)

except ValueError as error:
    print("Error controlado correctamente:", error)
