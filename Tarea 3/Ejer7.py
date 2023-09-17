#Declarlar la variable contraseña
password = "CarroRojo"
#Introducir
passwordinput = input("Ingrese contraseña: ")
#Converir a minuscula
passwordinput = passwordinput.lower()
# Comprobar datos
if passwordinput == password.lower():
    print("La Contraseña es igual")
else:
    print("La contraseña no coincide")
