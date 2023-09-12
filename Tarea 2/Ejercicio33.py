numero_mayor = -float("inf")

while True:
  numero = float(input("Ingrese un número: "))

  if numero > numero_mayor:
    numero_mayor = numero

  if numero == 0:
    break

print("El número mayor ingresado es:", numero_mayor)
