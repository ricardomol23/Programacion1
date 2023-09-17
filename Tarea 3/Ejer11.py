# Declarar las variables
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (Hombre/Mujer): ")

# Convertir el nombre a minúsculas
nombre = nombre.lower()

# Comprobar el sexo
if sexo == "hombre":
    # Si es hombre, comprobar si el nombre está después de la N
    if nombre > "n":
        # Si está después de la N, el grupo es B
        grupo = "B"
    else:
        # Si no está después de la N, el grupo es A
        grupo = "A"
else:
    # Si es mujer, el grupo es A
    grupo = "A"

# Mostrar el grupo
print("El grupo que le corresponde es:", grupo)
