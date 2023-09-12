total = 0
cantidad_productos = 0

while True:
  monto = float(input("Ingrese el monto de la compra: "))
  if monto == 0:
    break
  else:
    if monto < 0:
      print("El monto no puede ser negativo. Ingrese un nuevo monto.")
      continue
    else:
      total += monto
      cantidad_productos += 1

if total > 1000:
  descuento = total * 0.10
  total -= descuento

print("El total a pagar es de: $", total)
