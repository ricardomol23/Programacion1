def analizar_calificaciones():
  """
  Analiza las calificaciones de los alumnos.

  Returns:
    El porcentaje de alumnos aprobados y el promedio de los aprobados.
  """

  aprobados = 0
  total_calificaciones = 0
  promedio_aprobados = 0

  while True:
    respuesta = input("¿Desea analizar calificaciones? (S/N): ")
    if respuesta == "S":
      calificacion = float(input("Ingrese la calificación del alumno: "))
      if calificacion > 4:
        aprobados += 1
        promedio_aprobados += calificacion
      total_calificaciones += 1
    else:
      break

  porcentaje_aprobados = 100 * aprobados / total_calificaciones

  return porcentaje_aprobados, promedio_aprobados


if __name__ == "__main__":
  porcentaje_aprobados, promedio_aprobados = analizar_calificaciones()
  print("Porcentaje de alumnos aprobados:", porcentaje_aprobados)
  print("Promedio de los aprobados:", promedio_aprobados)
