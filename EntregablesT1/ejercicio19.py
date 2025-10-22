correctas = int(input("Número de respuestas correctas: "))
incorrectas = int(input("Número de respuestas incorrectas: "))
blanco = int(input("Número de respuestas en blanco: "))

nota_final = correctas * 5 + incorrectas * (-1) + blanco * 0

print("La nota final del estudiante es: ", nota_final)
