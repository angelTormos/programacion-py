salario_base = float(input('Introduce el salario '))
venta1 = float(input('Introduce la venta 1 '))
venta2 = float(input('Introduce la venta 2 '))
venta3 = float(input('Introduce la venta 3 '))

total_venta1 = (venta1 * 0.10)
total_venta2 = (venta2 * 0.10)
total_venta3 = (venta3 * 0.10)

total_comisiones = total_venta1 + total_venta2 + total_venta3
salario_total = salario_base + total_venta1 + total_venta2 + total_venta3

print("Comisiones =", total_comisiones , "\nTotal =", salario_total)