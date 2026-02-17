from pathlib import Path

usuario = input("Introduce un nombre de usuario: ")

ruta = f"/home/{usuario}"

dicc={}

if Path("users.txt").exists():
    with open("users.txt", "r") as f:
        for line in f.readlines():
            u,r = line.strip().split(",")
            dicc[u] = r

if usuario not in dicc:
    with open("users.txt", "a") as j:
        j.write(f"{usuario}, {ruta}\n")
else:
    print("El usuario ya existe")