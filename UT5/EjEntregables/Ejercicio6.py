import shutil

dir = {}

for i in range(3):
    ruta = input("Introduce una ruta: ")
    total, usado, libre = shutil.disk_usage(ruta)
    total_gb = round(total / 1024 ** 3 , 1)
    usado_gb = round(usado / 1024 ** 3, 1)
    libre_gb = (libre / 1024 ** 3, 1)
    dir[ruta] = "Espacio total: ", total, "espacio usado", usado, "espacio libre", libre

for key, values in dir.items():
    print ("Clave", key, "valor", values)