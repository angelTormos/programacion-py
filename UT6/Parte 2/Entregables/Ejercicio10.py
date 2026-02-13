import sys
from pathlib import Path

fichero = Path(sys.argv[1])
ruta = Path.cwd()/fichero

if ruta.exists():
    with open(ruta, "r") as f:
        lineas = 0
        for i in f.readlines():
            lineas += 1
        f.seek(0)
        cont_letras = 0
        for j in f:
            for letras in j:
                cont_letras += 1
        palabras = str(f).split(" ")
        contar_palabras = len(palabras)

else:
    print("El archivo no existe")

print(lineas)
print(contar_palabras)
print(cont_letras)
