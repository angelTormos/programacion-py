from pathlib import Path
dir_actual = Path.cwd()
contador = 0

for i in dir_actual.iterdir():
    if i.is_file():
        if i.suffix == ".log":
            contador += 1
        else:
            continue
    else:
        continue

print("Hay", contador, "archivos .log")