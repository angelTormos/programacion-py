d = float(input("Distancia entre los vehículos (km): "))
v1 = float(input("Velocidad del vehículo más lento (km/h): "))
v2 = float(input("Velocidad del vehículo más rápido (km/h): "))

t_horas = d / (v2 - v1)
t_minutos = t_horas * 60

print("El vehículo más rápido alcanzará al otro en", t_minutos ,"minutos.")
