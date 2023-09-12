print("Ejemplo usando un ciclo indefinido")
acomulador = 10
while acomulador > 0:
  print(acomulador)
  acomulador= acomulador - 1


print("Ejemplo usando recursividad")
def ciclo_recursivo(acomulador):
  if acomulador > 0:
    print(f"Voy en el ciclo:{acomulador}")
    ciclo_recursivo(acomulador-1)
  else:
    return
ciclo_recursivo(10)