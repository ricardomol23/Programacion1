# Declarar las variables
edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese sus ingresos mensuales: "))

# Comprobar si el usuario cumple los requisitos
if edad >= 16 and ingresos >= 1000:
    # El usuario tiene que tributar
    print("Tiene que tributar")
else:
    # El usuario no tiene que tributar
    print("No tiene que tributar")
