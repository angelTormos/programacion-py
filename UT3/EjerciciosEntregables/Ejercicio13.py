from pathlib import Path

directorio_actual = Path('.')

archivo_mas_reciente = None
fecha_mas_reciente = 0.0
archivos_encontrados = False

for elemento in directorio_actual.iterdir():
    
    if elemento.is_file():
        archivos_encontrados = True
        
        stats = elemento.stat()
        
        fecha_modificacion = stats.st_mtime
        
        if fecha_modificacion > fecha_mas_reciente:
            fecha_mas_reciente = fecha_modificacion
            archivo_mas_reciente = elemento.name

if archivos_encontrados:
    print("El archivo modificado más recientemente es: ", archivo_mas_reciente)
else:
    print("Sin archivos")