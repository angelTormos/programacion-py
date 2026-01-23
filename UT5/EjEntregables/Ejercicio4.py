from pathlib import Path

ruta_actual = Path.cwd()
dir = {}

for elemento in ruta_actual.iterdir():
    if elemento.is_file():
        dir[elemento] = "Es un fichero"
    else:
        dir[elemento] = "Es un directorio"


for key, value in dir.items():
    print (key, value)