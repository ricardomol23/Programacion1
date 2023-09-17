while True:
    respuesta = input("¿Desea continuar?").strip().upper()  # Lee la respuesta y la convierte a mayúsculas
    
    if respuesta != "SI":
        # El usuario no quiere continuar, así que preguntamos nuevamente
        continue
    else:
        # El usuario quiere continuar, así que salimos del bucle
        print("!HASTA LA VISTA¡")
        break

# El programa continúa aquí después de que el usuario responda "SI"
