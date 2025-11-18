base = float(input("Introduce la base (numero real) "))
exponente = int(input("Introduce el expoennte (entero positivo) "))
contador = 1
res = 1.0

while exponente < 0:
    exponente = int(input("Introduce el expoennte (entero positivo) "))

while contador <= exponente:
    res = res * base
    contador = contador + 1

print(res)