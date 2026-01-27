from pathlib import Path

ruta = Path("/home/angtorgua2/ejercicio7")

dicc = {}

for i in ruta.iterdir():
    if i.is_dir():
        dicc [i] = 0
    for j in i.iterdir():
        if j.is_dir():
            dicc [i] += 1

for usuario, carpetas in dicc.items():
    print ("El usuario", usuario, "tiene", carpetas, "carpetas")