import shutil
umbral = int(input("Introduce el umbral "))

if umbral > 100 or umbral < 0:
    for i in range(2):
        umbral = int(input("Introduce el umbral "))
        if umbral < 100 and umbral > 0:
            break
        else:
            continue
else:
    uso = shutil.disk_usage("/")
    porcentaje = uso.used / uso.total * 100

    if porcentaje < umbral:
        print("Estás dentro del umbral")
    else:
        print("Estás fuera del umbral")