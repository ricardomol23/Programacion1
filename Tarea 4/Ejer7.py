# Solicitar la cantidad objetivo para ahorrar
objetivo = float(input("Ingrese la cantidad objetivo que desea ahorrar: "))
total_ahorrado = 0

# Solicitar las cantidades a ahorrar hasta alcanzar el objetivo
while total_ahorrado < objetivo:
    cantidad = float(input("Ingrese la cantidad a ahorrar: "))
    total_ahorrado += cantidad

    # Mostrar el saldo actual
    print(f"Total ahorrado hasta ahora: {total_ahorrado} pesos")

print("¡Has alcanzado tu objetivo de ahorro!")
