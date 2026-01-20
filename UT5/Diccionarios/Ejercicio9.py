frases = []
contar_palabras = {}

for i in range(5):
    texto = input("Introduce una frase: ")
    texto = texto.lower()
    frase_div = texto.split()
    frases+= frase_div

for palabra in frases:
    if palabra not in contar_palabras:
        contar_palabras[palabra] = 1
    else:
        contar_palabras[palabra] += 1
print(contar_palabras)
