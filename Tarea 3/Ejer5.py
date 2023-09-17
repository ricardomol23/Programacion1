# Declarar las variables
horas = int(input("Ingrese el número de horas: "))
opcion = int(input("Ingrese la opción: "))

# Convertir las horas a días
dias = horas / 24

# Convertir los días a semanas
semanas = dias / 7

# Calcular las horas equivalentes
horasEquivalentes = horas % 24

# Imprimir el resultado
if opcion == 1:
    print("El número de semanas es:", semanas)
elif opcion == 2:
    print("El número de días es:", dias)
elif opcion == 3:
    print("El número de horas equivalentes es:", horasEquivalentes)
else:
    print("Opción no válida")
