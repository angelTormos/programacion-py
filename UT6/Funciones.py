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
    return base ** exp

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