def invertir_frase(frase):

  nueva_frase = ""
  for caracter_actual in frase:
    nueva_frase = caracter_actual + nueva_frase
  return nueva_frase


if __name__ == "__main__":
  frase = input("Ingrese una frase: ")
  nueva_frase = invertir_frase(frase)
  print("La frase invertida es:", nueva_frase)
