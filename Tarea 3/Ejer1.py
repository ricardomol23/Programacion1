# Solicitar el nombre al usuario
nombre = input("¿Cuál es tu nombre? ")

# Solicitar el primer apellido al usuario
apellido1 = input("¿Cuál es tu primer apellido? ")

# Almacenar el nombre y primer apellido en una nueva variable
fullName = nombre + " " + apellido1

# Solicitar la edad al usuario
edad = int(input("¿Cuántos años tienes? "))

# Calcular el año de nacimiento del usuario
year = 2023 - edad

# Mostrar el nombre completo y el año de nacimiento del usuario
print("Nombre completo:", fullName)
print("Año de nacimiento:", year)
