mensaje = input("Introduce un mensaje: ")

with open('palabras.txt', 'a') as f:
    f.write(f"{mensaje}\n")