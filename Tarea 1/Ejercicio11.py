def main():
    fecha = input("Ingresa una fecha en formato DD/MM/AAAA: ")

    if len(fecha) == 8:
        dia = fecha[:2]
        mes = fecha[2:4]
        year = fecha[4:]
        print(f"Fecha ingresada: {dia}/{mes}/{year}")
    else:
        print("Formato de fecha incorrecto.")

