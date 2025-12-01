from pathlib import Path

while True:
    archivo = input("Introduce el nombre de un archivo ")
    ruta_archivo = Path(archivo)
    
    if ruta_archivo.is_file():
        try:
            tamano_bytes = ruta_archivo.stat().st_size
            
            print("Archivo ", archivo, "encontrado")
            print("El tamaño del archivo es: ", tamano_bytes, " bytes.")
            
            break
            
        except Exception as e:
            print("Error al obtener la información del archivo: ",e,)
            
    else:
        print("Archivo ", archivo, " no encontrado o no es un archivo válido. Inténtalo de nuevo.")