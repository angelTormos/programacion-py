
while True:
    caracter = input("Introduce un caracter ")
    if len(caracter) != 1:
        print("Solo introduce un valor")ç
        continue
    else:
        if caracter in 'AEIOUaeiou':
            print("Vocal")
        elif caracter == " ":
            break
        else:
            print("No vocal")