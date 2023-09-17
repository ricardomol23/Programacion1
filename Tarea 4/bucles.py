# Declarar la variable
continuar = True

# Preguntar al usuario si desea terminar el programa
while continuar:
    respuesta = input("¿Desea terminar el programa? (S/N): ").upper()

    # Si la respuesta es N, terminar el bucle
    if respuesta == "N":
        continuar = False

    # Si la respuesta es S, mostrar un mensaje de error
    elif respuesta == "S":
        print("El programa se ha terminado")
        exit()

    # Si la respuesta no es S ni N, mostrar un mensaje de error
    else:
        print("Respuesta no válida")
