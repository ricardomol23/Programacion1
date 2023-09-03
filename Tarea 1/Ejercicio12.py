# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Verificar si el número es par
es_par = numero % 2 == 0

# Imprimir el resultado
if es_par:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} no es par.")