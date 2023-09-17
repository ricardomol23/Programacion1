# Solicitar el nombre al usuario y guardarlo en la variable 'nombre'
nombre = input("Por favor, ingrese su nombre: ")

# Solicitar el primer apellido al usuario y guardarlo en la variable 'apellido1'
apellido1 = input("Por favor, ingrese su primer apellido: ")

# Almacenar el nombre y primer apellido en la variable 'fullName'
fullName = nombre + " " + apellido1

# Solicitar la edad al usuario
edad_str = input("Por favor, ingrese su edad: ")

# Intentar convertir la edad a un número entero
try:
    edad = int(edad_str)

    # Calcular el año de nacimiento asumiendo que estamos en el año 2023
    year = 2023 - edad

    # Mostrar la información básica
    print("Nombre completo:", fullName)
    print("Año de nacimiento:", year)

    # Verificar las condiciones de descuento
    if edad < 18:
        year18 = year + 18
        print(f"Eres menor de edad, no podemos darte de alta hasta el año {year18}")
    elif 18 <= edad < 25:
        print("Tienes un 10% de descuento")
    elif edad == 18 or edad == 25:
        print("Premio, tienes un descuento especial del 20%")
    else:
        print("Lo sentimos, pero no tienes descuento")

except ValueError:
    # Manejar el error si la edad no es un número
    print("Hay un error, no hemos podido calcular tu edad")
    print("En el año de nacimiento: no puede calcularse")
