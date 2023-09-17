# Solicitar la edad al usuario
edad_str = input("Por favor, ingrese su edad: ")
edad = int(edad_str)
#Condicional de mayor de edad
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")