# Ejercicio 1

def mayor(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(mayor(7, 5))

# Ejercicio 3

def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(es_par(55))

# Ejercicio 6

def es_mayusculas(cad):
    if str(cad).isupper():
        return True
    else:
        return False
    
print(es_mayusculas('hrthrthtrht'))

# Ejercicio 7

def potencia(base, exp):
    if exp > 0:
        print("La potencia es", base ** exp)
    elif exp == 0:
        print("La potencia es 1")
    else:
        print("La potencia es", 1 / (base ** abs(exp)))
    
print(potencia(44, 5))

# Ejercicio 9

def ordena_mayor_menor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            return num1, num2, num3
        else:
            return num1, num3, num2
    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            return num2, num1, num3
        else:
            return num2, num3, num1
    else:
        if num1 >= num2:
            return num3, num1, num2
        else:
            return num3, num2, num1

print(ordena_mayor_menor(48, 2, 150))

# Ejercicio 10

import math

def clasifica_circunferencias(x1, y1, r1, x2, y2, r2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if distancia > (r1 + r2):
        print("Circunferencias exteriores")
    elif distancia == (r1 + r2):
        print("Circunferencias tangentes exteriores")
    elif distancia < (r1 + r2) and distancia > abs(r1 - r2):
        print("Circunferencias secantes")
    elif distancia == abs(r1 - r2):
        print("Circunferencias tangentes interiores")
    elif distancia > 0 and distancia < abs(r1 - r2):
        print("Circunferencias interiores")
    elif distancia == 0:
        print("Circunferencias concéntricas")

clasifica_circunferencias(123, 32, 4, 543, 564, 87)

# Ejercicio 11

def clasifica_triangulo(a,b,c):
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

clasifica_triangulo(32, 54, 32)

# Ejercicio 12

def es_bisiesto(anyo):
    if anyo % 4 == 0 :
        return True
    elif anyo % 100 != 0:
        return False
    elif anyo % 400 == 0:
        return True

print(es_bisiesto(2029))

# Ejercicio 13

def es_fecha_correcta(dia, mes, year):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_del_mes = 31
    #elif mes in [4, 6, 9, 11]:
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_del_mes = 30
    elif mes == 2:
        #  bisiesto
        if (year % 4 == 0 and not (year % 100 == 0)) or (year % 400 == 0):
            dias_del_mes = 29
        else:
            dias_del_mes = 28
    else:
        return False

    if dia < 1 or dia > dias_del_mes:
        return False
    else:
        return True

print(es_fecha_correcta(30, 11, 2028))

# Ejercicio 14

def calcula_ganancias_uva(precio_inicial, kilos, tipo, tamano):
            if tipo == "A":
                if tamano == "1":
                    precio_inicial += 20
                else:  
                    precio_inicial += 30
            elif tipo == "B":
                if tamano == "1":
                    precio_inicial -= 30
                else: 
                    precio_inicial -= 50

            precio_final = precio_inicial * kilos
            total = precio_final / 100
            return total

print(calcula_ganancias_uva(12, 150, "A", 1))

# Ejercicio 15

def costes_viaje(n):
    coste_por_alumno = 0.0
    coste_autobus = 0.0

    if n >= 100:
        coste_por_alumno = 65
    elif n >= 50:
        coste_por_alumno = 70
    elif n >= 30:
        coste_por_alumno = 95
    elif n > 0: 
        coste_por_alumno = 2850 / n

    coste_autobus = n * coste_por_alumno

    return coste_por_alumno, coste_autobus

print(costes_viaje(67))

# Ejercicio 16

def coste_llamada(tiempo, es_domingo, turno):
    coste = 0.0

    if tiempo <= 5:
        coste = tiempo * 100
    elif tiempo <= 8:
        coste = (tiempo - 5) * 80 + 500
    elif tiempo <= 10:
        coste = (tiempo - 8) * 70 + 240 + 500
    else:
        coste = (tiempo - 10) * 50 + 140 + 240 + 500

    if es_domingo == "S":
        coste += coste * 0.03
    else:
        if turno == "M":
            coste += coste * 0.15
        elif turno == "T":
            coste += coste * 0.10

    cost_total = coste / 100
    return cost_total

print(coste_llamada(120, "N", "M"))

# Ejercicio 18

def dia_escrito(dia):
    if dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miércoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sábado"
    elif dia == 7:
        return "Domingo"
    else:
        return "Día incorrecto"
    
print(dia_escrito(7))

# Ejercicio 19
def num_dias_mes(mes):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return "31 días"
    elif mes == 2:
        return "28 o 29 días"
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    #elif mes in [4, 6, 9, 11]:
        return "30 días"
    else:
        return "Mes incorrecto"

print(num_dias_mes(12))

# Ejercicio 20
def calcula_coste_transporte(peso, zona):      
    if peso > 0 and peso <= 5000:
        if zona == 1:
            return peso * 24 / 100
        elif zona == 2:
            return peso * 20 / 100
        elif zona == 3:
            return peso * 21 / 100
        elif zona == 4:
            return peso * 10 / 100
        elif zona == 5:
            return peso * 18 / 100
        else:
            return "Zona incorrecta."
    else:
        return "Peso incorrecto (no podemos transportar paquetes de más de 5Kg)."

print(calcula_coste_transporte(254, 4))

# Ejercicios para practicar bucles

# Ejercicio 1

def factorial(num):
    resultado = 1
    contador = 2

    while contador <= num:
        resultado *= contador
        contador += 1

    return resultado

print(factorial(6))

# Ejercicio 5

def pares_entre(num1, num2):
    if num1 % 2 == 1:
        num1 += 1

    while num1 <= num2:
        print(num1)
        num1+=2

pares_entre(2, 9)

# Ejercicio 6

def tabla_multiplicar(n):
    num=1
    while num<=10:
        print(f" {n} * {num} = {num * n}")
        num+=1

tabla_multiplicar(4)

# Ejercicio 10

def adivina_numero(intentos):
    import random

    num_secreto = random.randint(1, 100)

    print("Adivina el número (de 1 a 100):")

    num = int(input("Introduce un número: "))

    while num_secreto != num and intentos > 1:
        if num_secreto > num:
            print("Muy bajo")
        else:
            print("Muy alto")
        
        num = int(input("Introduce otro número: "))

    if num_secreto == num:
        print(f"CORRECTO: era el {num_secreto} y lo has adivinado en {11 - intentos} intentos.")
    else:
        print(f"¡Has perdido! El número era: {num_secreto}")

#adivina_numero(6)

# Ejercicio 11

def es_primo(n):
    import math

    es_primo = True

    if n <= 1:
        es_primo = False
    else:
        for div in range(2, int(math.sqrt(n)) + 1):
            if n % div == 0:
                es_primo = False
                return False
                break 
            
        else:
            return True

print(es_primo(6))

# Ejercicio 20

def primeros_primos(N):
    contador_primos = 0  
    numero = 2          

    while contador_primos < N:
        es_primo = True

        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                es_primo = False
                break

        if es_primo:
            print(numero)
            contador_primos += 1

        numero += 1