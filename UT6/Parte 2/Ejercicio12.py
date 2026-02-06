with open('frases.txt', 'w') as f:
    for i in range(3):
        texto = input("Introaduce una frase: ")
        f.write(f"{texto}\n")
    
for lines in texto:
    lines = f.readlines()

print(frases)