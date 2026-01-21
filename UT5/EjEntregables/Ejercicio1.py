import sys
import platform


ordenador = {
    'Sistema operativo' : sys.platform,
    'Version' : sys.version,
    'Nodo' : platform.node(),
    'Procesador' : platform.processor()
}

lista = []

for i in ordenador.values():
    lista.append(i)

lista.sort()
print(lista)