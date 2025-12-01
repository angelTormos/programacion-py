from pathlib import Path

while True:
    print("1) Listar archivos del directorio actual")
    print("2) Crear carpeta 'logs'")
    print("3) Salir")
    
    opcion = input("Introduce una opción (1, 2, o 3): ")
    
    if opcion == '1':
        directorio_actual = Path('.')
        print("Contenido del directorio actual:")
        encontrados = False
        
        for elemento in directorio_actual.iterdir():
            if elemento.is_file():
                print("ARCHIVO: ", elemento.name)
                encontrados = True
                
        if not encontrados:
            print("  (No se encontraron archivos en el directorio actual.)")
        
    elif opcion == '2':
        carpeta_logs = Path("logs")
        
        carpeta_logs.mkdir() 
        print("Carpeta logs creada con éxito.")
        
    elif opcion == '3':
        break
        
    else:
        print("Opción no válida. Por favor, introduce 1, 2 o 3.")