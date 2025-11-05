from pathlib import Path
import shutil

config = Path("config.ini")
ejemplo = Path("config.example.ini")

if not config.exists():
    if ejemplo.exists():
        shutil.copy(ejemplo, config)
        print("Archivo copiado")
    else:
        print("Falta el archivo de ejemplo")
else:
    print("Config existente")