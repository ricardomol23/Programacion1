# Solicitar la puntuación al usuario
puntuacion = float(input("Por favor, ingrese su puntuación: "))

# Determinar el nivel de rendimiento y calcular la cantidad de dinero
if puntuacion == 0.0:
    nivel_rendimiento = "Inaceptable"
    cantidad_dinero = 0.0
elif puntuacion == 0.4:
    nivel_rendimiento = "Aceptable"
    cantidad_dinero = 2400 * 0.4
elif puntuacion >= 0.6:
    nivel_rendimiento = "Meritorio"
    cantidad_dinero = 2400 * puntuacion
else:
    print("La puntuación ingresada no es válida. Debe ser 0.0, 0.4 o mayor a 0.6.")
    nivel_rendimiento = "Desconocido"
    cantidad_dinero = 0.0

# Mostrar el nivel de rendimiento y la cantidad de dinero
print(f"Su nivel de rendimiento es '{nivel_rendimiento}'.")
print(f"La cantidad de dinero que recibirá es {cantidad_dinero}€.")
