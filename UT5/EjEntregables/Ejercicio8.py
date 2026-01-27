from pathlib import Path
import platform
import os
from datetime import datetime

rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]
dicc = {}

for i in rutas:
    if Path(i).exists():
        if Path(i).is_dir():
            dicc [i] = "directorio"
        else:
            dicc [i] = "archivo"
    else:
        dicc [i] = "no existe"
    
so = platform.system()
cpu = os.cpu_count()
fecha = datetime.now()

print (f"El sistema operativo es {so}, tiene {cpu} CPUs, la fecha actual es {fecha}")

for archivo, estado in dicc.items():
    print (f"El la ruta {archivo} es un {estado}")