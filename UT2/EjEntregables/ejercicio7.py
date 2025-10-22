#Genera una contraseña de 10 caracteres: 4 letras + 4 dígitos + 2 símbolos de los siguientes '!#$%&*'. Sin bucles ni condicionales. 
# Utiliza la librería string para obtener las letras y los dígitos. Utiliza la librería random para seleccionar aleatoriamente un elemento de los anteriores (de las letras, de los números y de los símbolos especiales).

import string
import random

letras = string.ascii_letters
numeros = string.digits
simbolos = '!#$%&*'

letras_random = random.choices(letras, k=4)
numeros_random = random.choices(numeros, k=4)
simbolos_random = random.choices(simbolos, k=2)

total = letras_random + numeros_random + simbolos_random

contraseña = "".join(total)

print(contraseña)