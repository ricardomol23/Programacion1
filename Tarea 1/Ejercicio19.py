#Ingresar letra
letra = input("Ingresar una letra: ")

#Verificar longitud
if len(letra) > 1:
    print("No se puede procesar. Ingresaste mas de una letra: ")
else:
    #Convertimos la letra a minúscula
    letra = letra.lower()

    #Verificar si es una vocal
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Es una vocal")
    else:
        print("No es una vocal")