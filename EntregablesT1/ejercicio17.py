HH = int(input("Hora de salida (HH): "))
MM = int(input("Minutos de salida (MM): "))
SS = int(input("Segundos de salida (SS): "))
T = int(input("Tiempo de viaje (en segundos): "))

salida_segundos = HH * 3600 + MM * 60 + SS
llegada_segundos = salida_segundos + T
HH_llegada = (llegada_segundos // 3600) % 24
MM_llegada = (llegada_segundos % 3600) // 60
SS_llegada = llegada_segundos % 60

print(f"Hora de llegada: {HH_llegada}:{MM_llegada}:{SS_llegada}")
