from pathlib import Path

nombre = input("Introduce un nombre: ")

ruta = Path(f"/home/{nombre}")

with open('users.txt', 'a') as f:
    ruta_str = str(ruta)
    archivo = Path('users.txt')
    abierto = archivo.read_text()
    if ruta_str in abierto:
        print("El usuario ya exsite")
    else:
        f.write(f"{nombre}, {ruta}\n")
