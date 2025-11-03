import sys

hostname = sys.argv[1]

if hostname.startswith("PC-") and len(hostname) >= 7:
    print("VÁLIDO")
else:
    print("NO VÁLIDO")