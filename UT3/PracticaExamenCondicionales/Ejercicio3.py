import platform

so = platform.system()
version = platform.version()
procesador = platform.processor()

print(so, version, procesador)

if so == "Windows":
    print("winget")
elif so == "Linux":
    print("apt")
elif so == "macOS":
    print("brew")
else:
    print("Gestor no definido")