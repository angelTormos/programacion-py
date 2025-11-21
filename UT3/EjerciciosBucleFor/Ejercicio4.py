
for _ in range(10000000000):
    letra = input("Introduce una letra (espacio para salir) ")
    if letra == " ":
        break
    elif len(letra) != 1:
        print("Debes introducir una letra unicamente")
        break
    else:
        if letra in "aeiouAEIOU":
            print("VOCAL")
        else:
            print("NO VOCAl")

