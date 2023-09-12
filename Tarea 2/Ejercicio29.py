# Inicializar variables para el cálculo de promedios
suma_positivos = 0
suma_negativos = 0
contador_positivos = 0
contador_negativos = 0

# Solicitar al usuario que ingrese 6 números
for i in range(6):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    
    if numero >= 0:
        suma_positivos += numero
        contador_positivos += 1
    else:
        suma_negativos += numero
        contador_negativos += 1

# Calcular los promedios
if contador_positivos > 0:
    promedio_positivos = suma_positivos / contador_positivos
    print(f"Promedio de números positivos: {promedio_positivos}")
else:
    print("No se ingresaron números positivos.")

if suma_negativos > 0:
    print(f"La suma de números negativos: {suma_negativos}")
else:
    print("No se ingresaron números negativos")
