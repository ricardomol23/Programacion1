# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Inicializar una lista para almacenar los divisores
divisores = []

# Encontrar los divisores del número
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Imprimir los divisores
print(f"Los divisores de {numero} son: {divisores}")
