palabra = input("Introduce una palabra: ")
contar_letras = {}

for letra in palabra:
    if letra not in contar_letras:
        contar_letras[letra] = 1
    else:
        contar_letras[letra] += 1

print(contar_letras)