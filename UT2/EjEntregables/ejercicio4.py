#Dada la IP ' 192.168.001.010 ': limpia bordes, cuenta puntos, extrae el primer octeto (hasta primer '.') y último octeto (desde último '.').
#Imprime estos 2 octetos.

texto = ' 192.168.001.010 '
IP = texto.strip()
primer_octeto = IP.index(".")
segundo_octeto = IP.find(".", primer_octeto+1)
tercer_octeto = IP.find(".", segundo_octeto+1)

print(IP.strip())
print(IP.count("."))
print(IP[:primer_octeto])
print(IP[tercer_octeto +1 :])