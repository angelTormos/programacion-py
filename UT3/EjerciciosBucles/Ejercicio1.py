num = int(input("Introduce un numero "))
res = 1

while num > 0:
    res *= num
    num -= 1

print(res)