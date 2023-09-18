def validar(email):
    arroba="@"
    emailValido=False
    for c in email:
        if c==arroba:
            return True
    return False

 
direccion=input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")