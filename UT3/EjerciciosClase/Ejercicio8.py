nota = int(input("Introduce tu nota "))
edad = int(input("Introduce tu edad "))
sexo = input("Introduce tu sexo (F o M) ")

if nota >= 5 and edad >= 18 and sexo == "F":
    print("Aceptada")
elif nota >= 5 and edad >= 18 and sexo == "M":
    print("Posible")
else:
    print("No aceptada")