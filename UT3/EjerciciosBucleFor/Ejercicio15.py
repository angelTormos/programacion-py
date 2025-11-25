empleados = int(input("Introduce el numero de empleados "))
sueldo = int(input("Cuanto se paga la hora "))
coste_empresa = 0

for _ in range(empleados):
    hora_empleado = int(input("Cuantas horas ha trabajado? "))
    sueldo_total = sueldo * hora_empleado
    coste_empresa = sueldo_total + coste_empresa
    print("Cobras", sueldo_total,"€")
print("La empresa pagó", coste_empresa, "€")