#Dada una ruta como 'C:\\Users\\alumno\\Desktop\\proyecto', extrae: unidad 'C', usuario 'alumno' y carpeta 'Desktop' usando find/index y [:].
#Imprime cada uno de los valores.

ruta = 'C:\\Users\\alumno\\Desktop\\proyecto'

alumno = ruta.index('alumno')
desktop = ruta.index('Desktop')
proyecto = ruta.index('proyecto')

print(ruta[0:1])
print(ruta[alumno:desktop - 1])
print(ruta[desktop:proyecto - 1])
