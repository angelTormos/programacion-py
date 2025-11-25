precio_sem = 0
horas_sem = 0

for _ in range(6):
    horas = int(input("Introduce las horas trabajadas cada dia "))
    precio = int(input("Introduce el precio por hora "))
    precio_dia = precio * horas
    precio_sem = precio_sem + precio_dia
    horas_sem = horas + horas_sem


print("Ha trabajado", horas_sem, "horas esta semana")
print("Ha ganado", precio_sem, "€ esta semana")
