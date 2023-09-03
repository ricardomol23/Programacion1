# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Calculamos el valor absoluto
if numero < 0:
    valor_absoluto = numero * -1
else:
    valor_absoluto = numero

# Mostramos el valor absoluto
print(f"El valor absoluto de {numero} es {valor_absoluto}")
