diccionario = {}

for i in range(3):
    text= input("Introduce una clave-valor: ")
    clave,valor = text.split('-')
    diccionario[clave] = valor

print (diccionario)