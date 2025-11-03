import platform

so = platform.system()
version = platform.version()
procesador = platform.processor()

print(so, version, procesador)

if so == "Windows":
    print("winget")
elif so == "Linux":
    print("apt")
elif so == "Darwin":
    print("brew")
else:
    print("gestor no definido")