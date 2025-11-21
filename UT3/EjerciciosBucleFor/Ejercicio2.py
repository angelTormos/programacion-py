num = int(input("Introduce un numero "))
suma = num
cont = 1

for _ in range(10000):
    if num == 0:
        break
    else:
        num = int(input("Introduce un numero "))
        cont = cont + 1
        suma = num + suma
        media = suma / cont
        print(suma)
        print(media)