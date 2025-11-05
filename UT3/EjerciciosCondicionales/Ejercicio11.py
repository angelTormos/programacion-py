a=float(input("Introduce el primer lado "))
b=float(input("Introduce el segundo lado "))
c=float(input("Introduce el tercer lado "))

if a**2+b**2==c**2 or c**2+b**2==a**2 or c**2+a**2==b**2:
    print ("El triangulo es rectangulo")
else:
    print ("No es rectangulo")

if a==b==c:
    print ("El triangulo es equilátero")
elif a==b or b==c or c==a:
    print ("El triangulo es isosceles")
else:
    print ("El triangulo es escaleno")