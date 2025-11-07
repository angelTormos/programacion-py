rep = int(input("Introduce la cantidad de numeros: "))
cont = 0
mayor = 0
menor = 0
igual = 0

while cont < rep:
    num = int(input("Introduce un numero "))
    if num > 0 :
        mayor = mayor + 1
        cont = cont + 1
    elif  num < 0 :
        menor = menor + 1
        cont = cont + 1
    elif  num == 0 :
        igual = igual +1
        cont = cont + 1
    else:
        print("El valor introducido no es valido")

print("Hay", mayor, "mayores que 0.", menor, "menores que 0, y", igual, "iguales a 0")