frase = input ("Escribe una frase ")
resultado = frase

for vocal in "aeiouAEIOU":
    resultado = resultado.replace(vocal, "*")

print(frase)
print(resultado)