import shutil
import sys


if len (sys.argv) == 2:
    umbral = int(sys.argv[1])
else:
    print("Introduzca un unico parametro. Usando umbral por defecto 85")
    umbral = 85

uso = shutil.disk_usage("/")
porcentaje = uso.used / uso.total * 100

if porcentaje >= umbral:
    print("ALERTA")
else:
    print("OK")