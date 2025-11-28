from pathlib import Path

n = int(input("Introduce el numero de carpetas a crear"))
cont = 0

for i in range(n):
    cont += 1
    Path.mkdir(str('Backup', cont))