#Dado el texto ' pc -- aula - 07 \n' debes convertirlo a 'PC-AULA-07' sin usar condicionales ni bucles. Imprime el resultado.

texto = " pc -- aula - 07 \n"

normalizado = texto.strip().upper().replace(" ", "").replace("-","",1)

print(normalizado)