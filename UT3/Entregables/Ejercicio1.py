import shutil
import sys

umbral = int(sys.argv[1])
uso = shutil.disk_usage("/")
porcentaje = uso.used / uso.total * 100

if porcentaje >= umbral:
    print("ALERTA")
else:
    print("OK")