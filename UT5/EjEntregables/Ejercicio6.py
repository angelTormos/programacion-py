import shutil

dir = {}

for i in range(3):
    ruta = input("Introduce una ruta: ")
    total, usado, libre = shutil.disk_usage(ruta)
    total, usado, libre = total/1024 ^3 , usado/1024 ^ 3, libre/1024 ^ 3
    dir[ruta] = "Espacio total: ", total, "espacio usado", usado, "espacio libre", libre

for key, values in dir.items():
    print ("Clave", key, "valor", values)