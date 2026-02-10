total = ""

with open('nombres.txt', 'r') as f:
    archivo = f.readlines()

for lines in archivo:
    if len(total) < len(lines):
        total = lines

print(f"El nombre mas largo es {total}")