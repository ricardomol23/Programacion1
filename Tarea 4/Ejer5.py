while True:
    respuesta = input("¿Desea continuar?: ").strip()  # Lee la respuesta y elimina espacios en blanco
    if respuesta == "s" or respuesta =="S":
        # El usuario quiere continuar, continúa preguntando
        continue
    else:
        # El usuario quiere continuar, así que salimos del bucle
        print("!HASTA LA VISTA¡")
        break

# El programa continúa aquí después de que el usuario responda "SI"
