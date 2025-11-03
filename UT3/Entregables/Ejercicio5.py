from pathlib import Path
import os

directorio = Path.cwd()
print(directorio)
print(os.listdir(directorio))

logs = directorio / "logs"

if not logs.exists():
    logs.mkdir()
    print("Carpeta creada")
else:
    print("Carpeta ya existe")