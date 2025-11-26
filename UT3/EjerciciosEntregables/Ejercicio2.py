from pathlib import Path
dir_actual = Path.cwd()
tamaño_total = 0

for i in dir_actual.iterdir():
    if i.is_file():
        if i.suffix == ".log":
            tamaño = i.stat().st_size
            tamaño_total = tamaño + tamaño_total
        else:
            continue
    else:
        continue

if tamaño_total >= 1_048_576:
    print("ALTO VOLUMEN")
else:
    print("OK")

print(tamaño_total)