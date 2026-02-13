from pathlib import Path

carpeta = Path("logs")
contador = 0
for fichero in carpeta.glob("*.txt"):
    contador += 1

print(f"Hay {contador} fixeros .txt")