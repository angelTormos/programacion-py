import os

nombre = []
directorios = {}

for i in range(3):
    nombre.append(input("Introduce un nombre: "))
    user = (f"~{nombre[i]}")
    dir = os.path.expanduser(user)
    directorios[nombre[i]] = dir

print (directorios)