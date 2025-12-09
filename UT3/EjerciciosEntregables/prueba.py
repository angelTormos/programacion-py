
ip_base = input("Introduce una IP ")
rango_ini = int(input("Introduce el inicio del rango "))
rango_fin = int(input("Introduce el fin del rango "))
max_host = int(input("Introduce el maximo de hosts "))

for i in range(rango_ini, rango_fin + 1):
    print(f"{ip_base}{i}.1")
    for f in range(2, max_host + 1):
        if f % 5 == 0:
            continue
        else:
            print(f"{ip_base}{i}.{f}")
