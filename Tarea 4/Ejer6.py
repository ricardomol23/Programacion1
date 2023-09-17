while True:
    # Solicitar la primera contraseña
    contraseña1 = input("Ingrese la contraseña: ")

    # Solicitar la segunda contraseña
    contraseña2 = input("Ingrese la contraseña nuevamente: ")

    # Verificar si las contraseñas coinciden
    if contraseña1 == contraseña2:
        print("Contraseña confirmada. ¡Bienvenido!")
        break
    else:
        print("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")
