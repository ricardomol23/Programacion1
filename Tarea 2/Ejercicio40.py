def main():
  """
  Programa principal.
  """

  contador_lineas = 0
  contador_digitos = 0
  cadena = ""

  while True:
    titulo = input("Ingrese un titulo de libro: ")

    if titulo == "*":
      break

    if titulo == "/":
      contador_lineas += 1
      print("En la linea", contador_lineas, "se ingresaron", contador_digitos, "digitos numericos")
      contador_digitos = 0
      cadena = ""
      continue

    for caracter in titulo:
      if caracter.isdigit():
        contador_digitos += 1

    cadena += titulo + " "

  print("En la linea", contador_lineas, "se ingresaron", contador_digitos, "digitos numericos")


if __name__ == "__main__":
  main()
