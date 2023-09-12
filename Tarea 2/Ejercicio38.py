def analizar_cadena(cadena):
  """
  Analiza una cadena de caracteres y muestra información sobre su contenido.

  Args:
    cadena: La cadena a analizar.

  Returns:
    La cantidad de letras, simbolos y digitos de la cadena.
  """

  letras = 0
  simbolos = 0
  digitos = 0
  multiplos_4 = 0

  for caracter in cadena:
    if caracter.isalpha():
      letras += 1
    elif caracter.isdigit():
      digitos += 1
      if caracter in "02468":
        multiplos_4 += 1
    else:
      simbolos += 1

  return letras, simbolos, digitos, multiplos_4


if __name__ == "__main__":
  cadena = input("Ingrese una cadena de caracteres: ")

  letras, simbolos, digitos, multiplos_4 = analizar_cadena(cadena)

  print("La cadena contiene", letras, "letras,", simbolos, "simbolos y", digitos, "digitos.")
  print("De los digitos,", multiplos_4, "son múltiplos de 4.")