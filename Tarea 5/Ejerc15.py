def maximo(a, b):
    if a > b:  # Usar 'a' y 'b' en lugar de 'x' e 'y'
        return a
    else:
        return b

def minimo(a, b):
    if a < b:  # Usar 'a' y 'b' en lugar de 'x' e 'y'
        return a
    else:
        return b

# Programa principal
x = int(input("Un número: "))
y = int(input("Otro número: "))
print(maximo(x - 3, minimo(x + 2, y - 5)))
