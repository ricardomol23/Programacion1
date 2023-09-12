def numeros_pares_impares(numero):
  """
  Calcula la cantidad de digitos pares e impares de un numero.

  Args:
    numero: El numero a analizar.

  Returns:
    La cantidad de digitos pares e impares.
  """

  digitos_pares = 0
  digitos_impares = 0

  while numero > 0:
    digito = numero % 10
    if digito % 2 == 0:
      digitos_pares += 1
    else:
      digitos_impares += 1
    numero //= 10

  return digitos_pares, digitos_impares


def main():
  """
  Programa principal.
  """

  numero = int(input("Ingrese un numero: "))
  contador_multiplos_3 = 0

  while numero != -1:
    digitos_pares, digitos_impares = numeros_pares_impares(numero)
    print("El numero", numero, "tiene", digitos_pares, "digitos pares y", digitos_impares, "digitos impares.")
    if numero % 3 == 0:
      contador_multiplos_3 += 1
    numero = int(input("Ingrese un numero: "))

  print("La cantidad de numeros multiplos de 3 ingresados es:", contador_multiplos_3)


if __name__ == "__main__":
  main()
