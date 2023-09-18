# Función para calcular la suma de los dígitos de un número
def sumatoriaDigitos(numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumatoriaDigitos(numero // 10)

# Algoritmo para solicitar números al usuario
while True:
    numero = int(input("Ingrese un número (100 para terminar): "))

    # Si el número es 100, terminar el algoritmo
    if numero == 100:
        break

    # Mostrar la suma de los dígitos del número
    print("La suma de los dígitos de {} es {}".format(numero, sumatoriaDigitos(numero)))
