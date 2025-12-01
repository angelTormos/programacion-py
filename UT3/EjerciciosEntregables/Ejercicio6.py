from pathlib import Path

n = int(input("Introduce el numero de carpetas a crear"))
cont = 0

for i in range(n):
    cont += 1
    ruta = (f"Backup_{cont}")
    ruta_final = Path(ruta)
    ruta_final.mkdir()