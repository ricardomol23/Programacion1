# Solicitar la renta anual al usuario
renta_anual = float(input("Por favor, ingrese su renta anual en euros: "))

# Calcular el tipo impositivo según la renta
if renta_anual < 10000:
    tipo_impositivo = 5
elif 10000 <= renta_anual <= 20000:
    tipo_impositivo = 15
elif 20000 < renta_anual <= 35000:
    tipo_impositivo = 20
elif 35000 < renta_anual <= 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

# Mostrar el tipo impositivo correspondiente
print(f"Su renta anual es de {renta_anual} euros.")
print(f"El tipo impositivo que le corresponde es del {tipo_impositivo}%.")
