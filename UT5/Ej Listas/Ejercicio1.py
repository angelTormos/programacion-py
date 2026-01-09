import random
lista = [0] * 10

for i in range(len(lista)):
    lista[i] = random.randint(1, 10)

for num in lista:
    cuadrado = num ** 2
    cubo = num ** 3
    print('Numero:', num, 'Cuadrado:', cuadrado, 'Cubo:', cubo)