ip_base = input("Introduce la IP base (incluye el punto final, ej: 192.168.): ")
inicio_subred = int(input("Introduce el inicio del rango de subred: "))
fin_subred = int(input("Introduce el fin del rango de subred: "))
maximo_host = int(input("Introduce el máximo de hosts: "))

for subred in range(inicio_subred, fin_subred + 1):
    prefijo_red = ip_base + str(subred) + "."
    gateway = prefijo_red + "1"
    print("[SUBNET ", subred, "] GATEWAY: ", gateway) 
    print("Hosts Asignables:")
    
    for host in range(2, maximo_host + 1):
        if host % 5 != 0:
            ip_host = prefijo_red + str(host)
            print("  ", ip_host)

