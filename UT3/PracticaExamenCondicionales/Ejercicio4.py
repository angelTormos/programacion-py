import sys


if len(sys.argv) == 2:
    hostname = sys.argv[1]
    if hostname.startswith("PC-") and len(hostname) > 7:
        print("VALIDO")
    else:
        print("NO VALIDO")
else:
    print("Error, no se ha introducido un valor correcto")
    exit