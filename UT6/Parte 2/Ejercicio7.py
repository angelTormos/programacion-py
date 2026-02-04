with open('nombres.txt', 'r') as f:
    archivo = f.readlines()
    total = len(archivo)


print(f"La suma es {total}")