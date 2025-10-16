#Dado un nombre de archivo llamado 'backup_2025_09_03.tar.gz' extrae la fecha en formato '03-09-2025' (puedes extraer el año, mes y día y luego unirlos con guiones) e imprímela. Luego cambia a '.zip' el nombre del archivo original y muéstralo.

original = 'backup_2025_09_03.tar.gz'

inicio = original.find('_') + 1
final = original.find('.')

fecha = original[inicio:final]
partes = fecha.split('_')
fecha_final = f"{partes[2]}-{partes[1]}-{partes[0]}"

print(fecha_final)

posicion_ext = original.find('.')
nombre_archivo = original[:posicion_ext]
nombre_nuevo = nombre_archivo + '.zip'