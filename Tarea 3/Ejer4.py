# Declarar las variables
a = float(input("Ingrese el primer lado del triángulo: "))
b = float(input("Ingrese el segundo lado del triángulo: "))
c = float(input("Ingrese el tercer lado del triángulo: "))

# Comprobar si los lados forman un triángulo
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    # No se forma un triángulo
    print("Los lados ingresados no forman un triángulo")
else:
    # Se forma un triángulo

    # Comprobar si el triángulo es equilátero
    if a == b == c:
        print("El triángulo es equilátero")

    # Comprobar si el triángulo es isósceles
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles")

    # Comprobar si el triángulo es escaleno
    else:
        print("El triángulo es escaleno")
