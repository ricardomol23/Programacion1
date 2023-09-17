# Solicitar el nombre del estudiante
nombre = input("¿Cuál es el nombre del estudiante? ")

# Solicitar la nota del estudiante
nota = int(input("¿Cuál es la nota del estudiante? "))

# Comprobar la nota del estudiante
if nota < 5:
    # Mostrar la calificación de insuficiente
    calificacion = "insuficiente"
elif nota >= 5 and nota <= 7:
    # Mostrar la calificación de suficiente
    calificacion = "suficiente"
elif nota >= 7 and nota <= 9:
    # Mostrar la calificación de notable
    calificacion = "notable"
else:
    # Mostrar la calificación de sobresaliente
    calificacion = "sobresaliente"

# Mostrar la calificación del estudiante
print("El estudiante", nombre, "con nota", nota, "es", calificacion)
