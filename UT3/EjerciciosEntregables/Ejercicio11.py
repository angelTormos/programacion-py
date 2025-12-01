ip_base = input("Introduce la IP base (incluye el punto final, ej: 192.168.1.): ")

inicio = int(input("Introduce el número de inicio del rango: "))

fin = int(input("Introduce el número de fin del rango: "))

if inicio > fin:
    print("El inicio debe ser menor o igual al fin.")
else:
    print("IPs Pares en el Rango")
    for i in range(inicio, fin + 1):
        
        if i % 2 == 0:
            
            ip_completa = ip_base + str(i)
            print(ip_completa)

