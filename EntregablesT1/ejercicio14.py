num = int(input('Introduce un numero de dos cifras '))

unidades = num % 10
decenas = num // 10

invertido = unidades * 10 + decenas

print('El numero', num, 'al revés es', invertido)

