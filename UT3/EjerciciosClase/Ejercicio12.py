año=int(input("Introduce un año "))

if año % 4 == 0 :
    print ("Es bisiesto")
elif año % 100 != 0:
    print ("No es bisiesto")
elif año % 400 == 0:
    print ("Es bisiesto")