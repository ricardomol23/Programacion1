def reemplazar_caracter(frase, caracter):
  """
  Reemplaza todas las ocurrencias del carácter especificado por el símbolo *.

  Args:
    frase: La frase a modificar.
    caracter: El carácter a reemplazar.

  Returns:
    La frase modificada.
  """

  nueva_frase = ""
  for caracter_actual in frase:
    if caracter_actual == caracter:
      nueva_frase += "*"
    else:
      nueva_frase += caracter_actual
  return nueva_frase


if __name__ == "__main__":
  frase = input("Ingrese una frase: ")
  caracter = input("Ingrese el carácter a reemplazar: ")
  nueva_frase = reemplazar_caracter(frase, caracter)
  print("La frase modificada es:", nueva_frase)
