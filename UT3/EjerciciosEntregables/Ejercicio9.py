from pathlib import Path

nombre_aula = input("Introduce el nombre del aula (ej: A201): ")
num_equipos_str = input("Introduce el número de equipos M (ej: 15): ")
num_equipos = int(num_equipos_str)


ruta_aula = Path(nombre_aula)

if ruta_aula.exists() and ruta_aula.is_dir():
    print("La carpeta del aula '", nombre_aula, "' ya existía.", sep="")
else:
    ruta_aula.mkdir()
    print("Carpeta principal '", nombre_aula, "' creada con éxito.", sep="")


print("Creación de carpetas de PCs")

for i in range(1, num_equipos + 1):
    
    nombre_pc = f"PC-{str(i).zfill(2)}"
    
    ruta_pc = ruta_aula / nombre_pc
    
    if ruta_pc.exists() and ruta_pc.is_dir():
        print("La carpeta '", ruta_pc, "' ya existía.", sep="")
    else:
        ruta_pc.mkdir()
        print("Carpeta '", ruta_pc, "' creada con éxito.", sep="")

print("\nProceso terminado.")