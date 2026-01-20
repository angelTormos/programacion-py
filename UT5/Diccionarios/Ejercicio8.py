persona = {
    'Jorge': 19,
    'Alvaro' : 20,
    'Angel' : 21,
    'Sergio' : 52
}

print("El mas mayor es:", max(persona, key=persona.get))
print("El mas joven es:", min(persona, key=persona.get))