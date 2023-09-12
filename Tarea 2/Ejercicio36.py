def suma_digitos(numero):


  suma = 0

  while numero > 0:
    digito = numero % 10
    suma += digito
    numero //= 10

  return suma


if __name__ == "__main__":
  numero = int(input("Ingrese un numero: "))

  suma_digitos = suma_digitos(numero)

  print("La suma de los digitos del numero es:", suma_digitos)
