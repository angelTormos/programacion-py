dicc = {}

with open('paths.txt', 'w') as f:
    f.write(f"port=8080\nmode=prod\nuser=admin")

with open('paths.txt', "r") as j:
    for lines in j.readlines():
        clave, valor = lines.strip().split("=")
        dicc[clave] = valor

pregunta = input("Introduce una clave: ")

if pregunta in dicc:
    print(dicc[pregunta])
else:
    print("Error, la clave no existe")
