from pathlib import Path

cont_zip = 0
cont_targz = 0
cont_otros = 0

print("Introduce nombres de archivos de backup. Escribe 'FIN' para terminar.")

while True:
    nombre_archivo = input("Nombre del archivo: ")
    
    if nombre_archivo == 'FIN':
        break
    
    ruta = Path(nombre_archivo)
    
    extension = ruta.suffix.lower()
    
    if extension == '.zip':
        cont_zip += 1
        
    elif len(ruta.suffixes) >= 2:
        doble_extension = "".join(ruta.suffixes).lower()
        
        if doble_extension == '.tar.gz' or doble_extension == '.tgz':
            cont_targz += 1
        else:
            cont_otros += 1
            
    elif extension:
        cont_otros += 1
        
    else:
        cont_otros += 1

print("RESUMEN DE CLASIFICACIÓN")
print("Archivos .zip: ", cont_zip)
print("Archivos .tar.gz / .tgz: ", cont_targz)
print("Otras extensiones / Sin extensión: ", cont_otros)