from pathlib import Path
import os

dir = {}

for i in range(3):
    nombre = input("Introduce el nombre de una carpeta ")
    ruta_actual = Path.cwd()/nombre
    if ruta_actual.exists():
        dir[nombre] = "ya existia"
    else:
        os.mkdir(nombre)
        dir[nombre] = "no existia, se ha creado"

for key, value in dir.items():
    print(key, value)