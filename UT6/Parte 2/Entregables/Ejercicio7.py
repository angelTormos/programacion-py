from pathlib import Path
    
ruta = Path.cwd()

with open('users.txt', 'r') as f:
    for linea in f:
        lineas = linea.strip()
        usuario, ruta_total = lineas.split(",")
        ruta_final = Path(ruta_total.strip())
        with open('homes_check.txt', 'a') as j:
            if ruta_final.exists():
                j.write(f"{usuario} -> {ruta_total} -> OK\n")
            else:
                j.write(f"{usuario} -> {ruta_total} -> No existe\n")