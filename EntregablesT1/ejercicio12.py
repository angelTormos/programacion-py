import math

x1 = float(input('Introduce el primer numero '))
x2 = float(input('Introduce el segundo numero '))
y1 = float(input('Introduce el tercero numero '))
y2 = float(input('Introduce el cuarto numero '))

distancia = math.sqrt(((x2 - x1)**2) + ((y2-y1)**2))

print('La distancia es de', distancia)