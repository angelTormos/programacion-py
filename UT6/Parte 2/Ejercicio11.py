contador = 0
with open('palabras.txt', 'r') as f:
    palabras = f.readlines()

for lines in palabras:
    print(lines)
    contador +=1


print(f"Hay {contador} palabras")