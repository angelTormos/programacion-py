examen_parcial1 = float(input('Introduce la nota del primer parcial: '))
examen_parcial2 = float(input('Introduce la nota del segundo parcial: '))
examen_parcial3 = float(input('Introduce la nota del tercer parcial: '))
examen_final = float(input('Introduce la nota del examen final: '))
trabajo_final = float(input('Introduce la nota del trabajo final: '))

media_parciales = (examen_parcial1 + examen_parcial2 + examen_parcial3) / 3
porcentaje_parciales = media_parciales * 0.55
porcentaje_final = examen_final * 0.30
porcentaje_trabajo = trabajo_final * 0.15

nota_final = porcentaje_parciales + porcentaje_final + porcentaje_trabajo

print('Tu nota final es', nota_final)