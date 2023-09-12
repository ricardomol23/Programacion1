# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero para calcular su factorial: "))

# Inicializar el resultado a 1
factorial = 1

# Calcular el factorial utilizando un bucle for
for i in range(1, n + 1):
    factorial *= i

# Imprimir el resultado
print(f"El factorial de {n} es {factorial}")
