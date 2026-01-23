from pathlib import Path

dir = {}

for i in range(4):
    texto = input("Introduce un directorio o fichero ")
    directorio = Path.cwd()/texto
    if directorio.exists():
        if directorio.is_file():
            dir[directorio] = "Es un fichero"
        else:
            dir[directorio] = "Es un directorio"
    else:
        dir[directorio] = "No existe"

for key, value in dir.items():
    print (key, value)
