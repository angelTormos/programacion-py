for i in range(5):
    nombre= input("Introduce un nombre: ")
    with open('nombres.txt', 'a') as f:
        f.write(f"{nombre}\n")
