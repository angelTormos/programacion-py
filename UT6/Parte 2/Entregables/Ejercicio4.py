from pathlib import Path

with open('paths.txt', 'w') as f:
    f.write(f"/lib/var\n/etc/hosts\n/home/alumno\n/home/angtorgua2/Baixades")

fichero = Path("paths.txt")
leer = fichero.read_text(encoding="utf-8")

with open('paths_status.txt', 'w') as j:
    for ruta in leer.splitlines():
        ruta_completa = Path(ruta)
        if ruta_completa.is_file():
            j.write(f"{ruta_completa} -> archivo\n")
        elif ruta_completa.is_dir():
            j.write(f"{ruta_completa} -> directorio\n")
        elif not ruta_completa.exists():
            j.write(f"{ruta_completa} -> no existe\n")
        else:
            j.write(f"{ruta_completa} -> otro\n")