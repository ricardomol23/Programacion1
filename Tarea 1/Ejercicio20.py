#Ingresar valores
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
#Inicializar variables
#menor = numero1 #Tengo duda de porque inicializar la variable
#Ciclo
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
else:
    menor = numero3

#Mostramos el resultado
print(f"El número menor es: {menor}")