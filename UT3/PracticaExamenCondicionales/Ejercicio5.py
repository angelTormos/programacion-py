from pathlib import Path
import os

directorio = Path.cwd()

print(directorio)
print(os.listdir(directorio))

log =  directorio / "log"

if log.exists():
    print("Carpeta ya existe")
else:
    log.mkdir()
    print("Carpeta creada")