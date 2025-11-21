cant = int(input("Introduce la cantidad de numeros a introducir "))
pos = 0
neg = 0
zero = 0


for i in range(cant):
    num = float(input("Introduce un numero "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    elif num == 0:
        zero =+1
    else:
        print("Introduce un valor valido ")

print("Hay", pos, "mayores que 0 |", neg, "menores que 0 y", zero, "iguales a 0")
