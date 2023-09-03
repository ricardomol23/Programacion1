#Ingresar año
year = int(input("Ingrese año: "))

#Validar si es biciesto
bisiesto = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Mostrar el resultado
if bisiesto:
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")