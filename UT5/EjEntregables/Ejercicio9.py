path = "/usr/local/bin:/usr/bin:/bin"

lista = path.split(":")

inicio = input("Introduce una ruta: ")
fin = input("Introduce otra ruta: ")

lista.insert(0, inicio)
lista.append(fin)

for i in lista:
    print(i)

unido = ':'.join(lista)

print(unido)