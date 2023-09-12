def construir_string():
  """
  Construye un string a partir de la entrada del usuario.

  Returns:
    El string completo.
  """

  string = ""

  while True:
    caracter = input("Ingrese un carácter: ")
    if len(caracter) != 1 or caracter == "0":
      break
    string += caracter

  return string


def porcentaje_letra_a(string):
  cantidad_letras_a = string.count("a")
  total_caracteres = len(string)

  return 100 * cantidad_letras_a / total_caracteres


if __name__ == "__main__":
  string = construir_string()
  porcentaje_a = porcentaje_letra_a(string)

  print("El string completo es:", string)
  print("El porcentaje de caracteres de la letra 'a' es:", porcentaje_a)
