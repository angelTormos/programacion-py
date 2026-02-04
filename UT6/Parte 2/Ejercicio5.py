with open('numeros.txt', 'r') as f:
    archivo = f.readlines()


for line in archivo:
    palabra = line.strip()
    numero = int(palabra)
    if numero % 2 == 0:
        print(numero)


