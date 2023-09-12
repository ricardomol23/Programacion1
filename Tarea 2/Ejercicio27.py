# Inicializar los dos primeros números de Fibonacci
fibonacci = [0, 1]

# Generar los siguientes 8 números de Fibonacci
for i in range(2, 10):
    siguiente_numero = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(siguiente_numero)

# Imprimir la secuencia de Fibonacci
print("Los primeros 10 números de Fibonacci son:", fibonacci)