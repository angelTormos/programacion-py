contador = 0

with open("admin_log.txt", 'r') as f:
    for i in f.readlines():
        contador += 1
        ult = i

print(f"El archivo contiene {contador} lineas")
print(ult)