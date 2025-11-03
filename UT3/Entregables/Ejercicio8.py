import sys
from pathlib import Path

archivo = Path(sys.argv[1])
tam = archivo.stat().st_size

if tam >= 1_048_576:
    print("GRANDE")
else:
    print("PEQUEÑO")