
objetivo = float(input("Ingrese la cantidad objetivo que desea ahorrar: "))
while objetivo < 0:
        print("Por favor, escriba una cantidad positiva.")
        objetivo = float(input("¿Cuántos quiere ahorrar?: "))

ahorrado = 0.0
while objetivo > ahorrado:
        ahorro = float(input("¿Cuánto quiere meter ahorrar?: "))
        while ahorro < 0:
            print("Por favor, escriba una cantidad positiva.")
            ahorro = float(input("¿Cuánto quiere meter ahorrar?: "))
        ahorrado += ahorro

print(f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} Pesos.")
