diccionario = {
    'python': 'Lenguaje de programación',
    'algoritmo': 'Conjunto de instrucciones',
    'variable': 'Espacio de memoria para almacenar datos'
}

palabra = input("Introduce una palabra del diccionario: ")

print(diccionario.get(palabra, 'La palabra no está en el diccionario'))