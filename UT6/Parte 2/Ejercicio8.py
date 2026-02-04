with open('nombres.txt', 'r') as f:
    archivo = f.readlines()

for lines in archivo:
    total = len(lines)

print(f"El nombre mas largo es {total}")