ip_base = input("Introduce la IP base (incluye el punto final, ej: 192.168.): ")
inicio_subred_str = input("Introduce el inicio del rango de subred: ")
fin_subred_str = input("Introduce el fin del rango de subred: ")
maximo_host_str = input("Introduce el máximo de hosts: ")

inicio_subred = int(inicio_subred_str)
fin_subred = int(fin_subred_str)
maximo_host = int(maximo_host_str)


for subred in range(inicio_subred, fin_subred + 1):
    prefijo_red = ip_base + str(subred) + "."
    gateway = prefijo_red + "1"
    print("[SUBNET ", subred, "] GATEWAY: ", gateway) 
    print("Hosts Asignables:")
    
    for host in range(2, maximo_host + 1):
        if host % 5 != 0:
            ip_host = prefijo_red + str(host)
            print("  ", ip_host)

