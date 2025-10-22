#Dado el email 'admin.redes@centro.edu', extrae el usuario (antes de '@'), el dominio (entre '@' y primer '.') y el tld (después del '.'). No uses bucles.~

email = 'admin.redes@centro.edu'

usuario = email.index("@")
dominio = email.find(".", usuario+1)
tld = email.find(".", dominio+1)

print(email[:usuario])
print(email[usuario+1:dominio])
print(email[dominio +1:])