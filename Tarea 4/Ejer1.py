while True:
    respuesta = input("¿Desea continuar? (Sí/No): ").strip()  # Lee la respuesta y elimina espacios en blanco
    
    if respuesta == "sí":
        # El usuario quiere continuar, continúa preguntando
        continue
    elif respuesta == "no":
        # El usuario no quiere continuar, así que rompemos el bucle
        break
    else:
        print("Respuesta incorrecta. Por favor, responda 'Sí' o 'No'.")

# El programa continúa aquí después de que el usuario responda "no"
print("Hasta la vista")
