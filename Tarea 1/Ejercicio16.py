#Solicitar nombres
name1 = input("Ingrese su primer nombre: ")
name2 = input("Ingrese el primer nombre de otra persona: ")

#Validar letra inicial y final
primera_letra =  name1[0].lower() == name2[0].lower()
segunda_letra = name1[-1].lower() == name2[-1].lower()

# Mostrar el resultado
if primera_letra or segunda_letra:
    print("True")
else:
    print("False")