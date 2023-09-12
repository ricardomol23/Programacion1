#ingresar texto
texto = input("Ingrese un texto: ")

#Convertir en minusculas
texto = texto.lower()

#Contador vocales
contador_vocales = 0

for caracter in texto:
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        contador_vocales += 1

print("Cantidad de vocale en el texto", contador_vocales)