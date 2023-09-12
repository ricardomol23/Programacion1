def main():
  """
  Programa principal.
  """

  cadena_multiplos_3 = ""
  cadena_con_0 = ""

  while True:
    numero = input("Ingrese un numero: ")

    if numero.isdigit() and numero != "10" and numero >= 0:
      cantidad_digitos = len(numero)
      contiene_0 = False

      for caracter in numero:
        if caracter == "0":
          contiene_0 = True
          break

      if cantidad_digitos % 3 == 0 or contiene_0:
        if cantidad_digitos % 3 == 0:
          cadena_multiplos_3 += numero + ";"
        if contiene_0:
          cadena_con_0 += numero + ";"

    if numero == "10" or numero < 0:
      break

  print("Los numeros con cantidad de digitos multiplos de 3 son:", cadena_multiplos_3)
  print("Los numeros que contienen el digito 0 son:", cadena_con_0)


if __name__ == "__main__":
  main()
