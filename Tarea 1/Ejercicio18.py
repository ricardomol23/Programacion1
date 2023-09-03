#Ingresar valores
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el primer número: "))

#Ciclo
if numero1 > numero2:
    mayor = numero1
elif numero2 > numero1:
    mayor = numero2
else:
    mayor = "Ambos números son iguales"

#Mostramos el resultado
print(f"El número mayor es: {mayor}")