#Vamos a generar un nombre de usuario. Dado un nombre=' Ana ' y un apellido=' López ' genera su usuario con las primeras 3 letras del nombre + las 3 primeras letras de su apellido + dos dígitos aleatorios. 
#Ten en cuenta que el nombre de usuario no puede tener vocales con acentos. Suponemos que sólo existen acentos en español

import random
import string

nombre = ' Ana '
apellido = ' López '

nombre_limpio = nombre.strip()
apellido_limpio = apellido.strip()

nombre_sin_acento = nombre_limpio.replace('á', 'a').replace('Á', 'A').replace('é', 'e').replace('É', 'E').replace('í', 'i').replace('Í', 'I').replace('ó', 'o').replace('Ó', 'O').replace('ú', 'u').replace('Ú', 'U')
apellido_sin_acento = apellido_limpio.replace('á', 'a').replace('Á', 'A').replace('é', 'e').replace('É', 'E').replace('í', 'i').replace('Í', 'I').replace('ó', 'o').replace('Ó', 'O').replace('ú', 'u').replace('Ú', 'U')

parte_nombre = nombre_sin_acento[:3].lower()
parte_apellido = apellido_sin_acento[:3].lower()

digitos_random = random.choices(string.digits, k=2)

digitos_str = "".join(digitos_random)

usuario = parte_nombre + parte_apellido + digitos_str

print(f"El nombre de usuario generado es: {usuario}")