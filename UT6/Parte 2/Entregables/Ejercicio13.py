from pathlib import Path

carpeta = Path("logs")

for fichero in carpeta.glob("*.log"):
    print(fichero)