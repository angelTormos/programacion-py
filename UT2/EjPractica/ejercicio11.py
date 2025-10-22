nombre = input("Introduce tu nombre ")

print(nombre.upper())
print(nombre.lower())
print(nombre.title())

no_espacios = nombre.replace(" ", "")
print(len(no_espacios))