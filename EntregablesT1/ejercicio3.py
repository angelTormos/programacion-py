import math

cateto1 = int(input("Introduce el primer cateto "))
cateto2 = int(input("Introduce el segundo cateto "))

hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))

print("La hipotenusa es igual a:", hipotenusa)