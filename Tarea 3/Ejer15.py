# Declarar las variables
vegetariana = False
ingrediente = ""

# Preguntar al usuario si quiere una pizza vegetariana
vegetariana = input("¿Quiere una pizza vegetariana? (S/N): ").upper()

# Si el usuario quiere una pizza vegetariana, mostrar el menú de ingredientes vegetarianos
if vegetariana == "S":
    ingredientes = ["Pimiento", "Tofu"]
else:
    # Si el usuario quiere una pizza no vegetariana, mostrar el menú de ingredientes no vegetarianos
    ingredientes = ["Pepperoni", "Jamón", "Salmón"]

# Solicitar al usuario que elija un ingrediente
ingrediente = input("Elija un ingrediente: ")

# Comprobar si el ingrediente elegido es válido
if ingrediente not in ingredientes:
    print("Ingrediente no válido")
    exit()

# Mostrar la pizza elegida
print("La pizza elegida es:")
if vegetariana:
    print("Pizza vegetariana con:", ingrediente)
else:
    print("Pizza no vegetariana con:", ingrediente)
