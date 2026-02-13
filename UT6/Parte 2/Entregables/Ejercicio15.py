from pathlib import Path

carpeta = Path("logs")

for fichero in carpeta.glob("*.log"):
    tamaño = fichero.stat().st_size
    print(f"{fichero} - {tamaño} bytes")