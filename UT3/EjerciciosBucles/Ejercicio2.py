num = int(1)
sum = 0
cont = 0

while num != 0:
    num = int(input("Introduce un numero (0 para salir) "))
    if num == 0: 
        continue
    sum = sum + num
    cont = cont + 1
    media = (sum / cont)
    print("Suma:", sum)
    print("Media: ", media)