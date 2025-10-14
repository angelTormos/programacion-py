#Dada la etiqueta 'PC-AULA-23', verifica si empieza por 'PC-' (solo muestra True o False) y extrae 'AULA' y '23' usando find y [:] (troceado de cadenas).
# No uses condicionales; solo imprime las partes obtenidas.

texto = "PC-AULA-23"

posc1 = texto.find('-')
resto = texto[posc1+1:]
posc2 = resto.find('-')

print(texto.startswith("PC-"))
print(resto[:posc2])
print(resto[posc2+1:])