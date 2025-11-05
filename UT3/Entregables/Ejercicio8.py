import sys
from pathlib import Path


if len (sys.argv) == 2:
    archivo = Path(sys.argv[1])
    tam = archivo.stat().st_size
    if tam >= 1_048_576:
        print("GRANDE")
    else:
        print("PEQUEÑO")
else:
    print("Error, no se ha introducido un unico parametro")
    exit