suma = 0

with open('numeros.txt', 'r') as f:
    archivo = f.readlines()


for line in archivo:
    numeros = line.strip()
    suma += int(numeros)


print(f"La suma es {suma}")