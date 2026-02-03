# Ejercicio 1
def mayor(n1, n2):
    resultado = n1 if n1 > n2 else n2
    return f"El número mayor entre {n1} y {n2} es {resultado}"

# Ejercicio 3
def es_par(n):
    resultado = n % 2 == 0
    return f"El número {n} es par: {resultado}"

# Ejercicio 6
def es_mayusculas(cad):
    resultado = str(cad).isupper()
    return f"La cadena '{cad}' está en mayúsculas: {resultado}"

# Ejercicio 7
def potencia(base, exp):
    if exp > 0:
        resultado = base ** exp
    elif exp == 0:
        resultado = 1
    else:
        resultado = 1 / (base ** abs(exp))
    return f"La potencia de {base} elevado a {exp} es {resultado}"

# Ejercicio 9
def ordena_mayor_menor(num1, num2, num3):
    numeros = sorted([num1, num2, num3], reverse=True)
    ordenados = (numeros[0], numeros[1], numeros[2])
    return f"Los números ({num1}, {num2}, {num3}) ordenados de mayor a menor son: {ordenados[0]}, {ordenados[1]}, {ordenados[2]}"

# Ejercicio 10
import math
def clasifica_circunferencias(x1, y1, r1, x2, y2, r2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    clasificacion = ""
    suma_radios = r1 + r2
    resta_radios_abs = abs(r1 - r2)

    if distancia > suma_radios:
        clasificacion = "exteriores"
    elif distancia == suma_radios:
        clasificacion = "tangentes exteriores"
    elif distancia < suma_radios and distancia > resta_radios_abs:
        clasificacion = "secantes"
    elif distancia == resta_radios_abs:
        clasificacion = "tangentes interiores"
    elif distancia > 0 and distancia < resta_radios_abs:
        clasificacion = "interiores"
    elif distancia == 0:
        clasificacion = "concéntricas"
    
    return f"La clasificación de las circunferencias (R1={r1}, R2={r2}, Distancia={distancia:.2f}) es: {clasificacion}"

# Ejercicio 11
def clasifica_triangulo(a,b,c):
    tipo_angulo = ""
    if a**2+b**2==c**2 or c**2+b**2==a**2 or c**2+a**2==b**2:
        tipo_angulo = "rectángulo"
    else:
        tipo_angulo = "no es rectángulo"

    tipo_lado = ""
    if a==b==c:
        tipo_lado = "equilátero"
    elif a==b or b==c or c==a:
        tipo_lado = "isósceles"
    else:
        tipo_lado = "escaleno"
        
    return f"El triángulo de lados ({a}, {b}, {c}) es {tipo_lado} y es de tipo {tipo_angulo}"

# Ejercicio 12
def es_bisiesto(anyo):
    resultado = (anyo % 4 == 0 and not (anyo % 100 == 0)) or (anyo % 400 == 0)
    return f"El año {anyo} es bisiesto: {resultado}"

# Ejercicio 13
def es_fecha_correcta(dia, mes, year):
    dias_del_mes = 0
    es_bisiesto_local = (year % 4 == 0 and not (year % 100 == 0)) or (year % 400 == 0)
    resultado = False
    
    if mes < 1 or mes > 12:
        resultado = False
    else:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias_del_mes = 31
        elif mes in [4, 6, 9, 11]:
            dias_del_mes = 30
        elif mes == 2:
            dias_del_mes = 29 if es_bisiesto_local else 28

        if dia >= 1 and dia <= dias_del_mes:
            resultado = True
        
    return f"La fecha {dia}/{mes}/{year} es correcta: {resultado}"

# Ejercicio 14
def calcula_ganancias_uva(precio_inicial, kilos, tipo, tamano):
            aumento = 0
            if tipo == "A":
                if tamano == "1":
                    aumento = 20
                else:  
                    aumento = 30
            elif tipo == "B":
                if tamano == "1":
                    aumento = -30
                else: 
                    aumento = -50

            precio_ajustado = precio_inicial + aumento
            precio_final = precio_ajustado * kilos
            ganancia_euros = precio_final / 100
            
            return f"Ganancia de la uva (Tipo {tipo}, Tamaño {tamano}, {kilos}Kg, Precio base {precio_inicial}c/Kg): {ganancia_euros:.2f}€"

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
        coste_autobus = 2850.0
        coste_por_alumno = coste_autobus / n
        
    coste_autobus = n * coste_por_alumno

    return f"Para {n} alumnos, el coste por alumno es {coste_por_alumno:.2f}€ y el coste total del autobús es {coste_autobus:.2f}€"

# Ejercicio 16
def coste_llamada(tiempo, es_domingo, turno):
    coste_base = 0.0

    if tiempo <= 5:
        coste_base = tiempo * 100
    elif tiempo <= 8:
        coste_base = (tiempo - 5) * 80 + 500
    elif tiempo <= 10:
        coste_base = (tiempo - 8) * 70 + 240 + 500
    else:
        coste_base = (tiempo - 10) * 50 + 140 + 240 + 500

    recargo = 0.0
    recargo_txt = ""
    if es_domingo == "S":
        recargo = 0.03
        recargo_txt = "3% por ser Domingo"
    else:
        if turno == "M":
            recargo = 0.15
            recargo_txt = "15% por Turno de Mañana"
        elif turno == "T":
            recargo = 0.10
            recargo_txt = "10% por Turno de Tarde"

    coste_final_centimos = coste_base * (1 + recargo)
    coste_euros = coste_final_centimos / 100
    
    return f"El coste de la llamada de {tiempo} minutos (Recargo: {recargo_txt}) es de {coste_euros:.2f}€"

# Ejercicio 18
def dia_escrito(dia):
    nombre_dia = ""
    if dia == 1:
        nombre_dia = "Lunes"
    elif dia == 2:
        nombre_dia = "Martes"
    elif dia == 3:
        nombre_dia = "Miércoles"
    elif dia == 4:
        nombre_dia = "Jueves"
    elif dia == 5:
        nombre_dia = "Viernes"
    elif dia == 6:
        nombre_dia = "Sábado"
    elif dia == 7:
        nombre_dia = "Domingo"
    else:
        nombre_dia = "Día incorrecto (debe ser entre 1 y 7)"
        
    return f"El día número {dia} de la semana es: {nombre_dia}"

# Ejercicio 19
def num_dias_mes(mes):
    dias = ""
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = "31 días"
    elif mes == 2:
        dias = "28 o 29 días (depende de si el año es bisiesto)"
    elif mes in [4, 6, 9, 11]:
        dias = "30 días"
    else:
        dias = "Mes incorrecto (debe ser entre 1 y 12)"
        
    return f"El mes número {mes} tiene: {dias}"

# Ejercicio 20
def calcula_coste_transporte(peso, zona):      
    coste_por_kg = 0.0
    zona_txt = ""
    
    if peso <= 0 or peso > 5000:
        return f"Cálculo de coste para {peso}g y Zona {zona}: Peso incorrecto (Máximo 5Kg o 5000g)."
    
    if zona == 1:
        coste_por_kg = 24
        zona_txt = "Zona 1 (América del Norte)"
    elif zona == 2:
        coste_por_kg = 20
        zona_txt = "Zona 2 (América Central)"
    elif zona == 3:
        coste_por_kg = 21
        zona_txt = "Zona 3 (América del Sur)"
    elif zona == 4:
        coste_por_kg = 10
        zona_txt = "Zona 4 (Europa)"
    elif zona == 5:
        coste_por_kg = 18
        zona_txt = "Zona 5 (Asia)"
    else:
        return f"Cálculo de coste para {peso}g y Zona {zona}: Zona incorrecta (debe ser entre 1 y 5)."

    coste_total_euros = (peso * coste_por_kg) / 1000 
    
    return f"El coste de transporte para {peso}g a la {zona_txt} es de {coste_total_euros:.2f}€"

# --- Ejercicios Bucles ---

# Ejercicio 1
def factorial(num):
    resultado = 1
    contador = 2

    while contador <= num:
        resultado *= contador
        contador += 1
    return f"El factorial de {num} es {resultado}"

# Ejercicio 5
def pares_entre(num1, num2):
    lista_pares = []
    
    inicio = num1 if num1 % 2 == 0 else num1 + 1

    while inicio <= num2:
        lista_pares.append(inicio)
        inicio += 2
        
    return f"Los números pares entre {num1} y {num2} (ambos inclusive) son: {', '.join(map(str, lista_pares))}"

# Ejercicio 6
def tabla_multiplicar(n):
    tabla = []
    num=1
    while num<=10:
        tabla.append(f" {n} * {num} = {num * n}")
        num+=1
    
    return f"La tabla de multiplicar del {n} es:\n" + "\n".join(tabla)

# Ejercicio 10 (Función Interactiva)
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
        
# Ejercicio 11
def es_primo(n):
    import math

    es_primo_val = True

    if n <= 1:
        es_primo_val = False
    else:
        for div in range(2, int(math.sqrt(n)) + 1):
            if n % div == 0:
                es_primo_val = False
                break
            
    return f"El número {n} es primo: {es_primo_val}"

# Ejercicio 20
def primeros_primos(N):
    contador_primos = 0  
    numero = 2
    primos_encontrados = []

    while contador_primos < N:
        es_primo_val = True

        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                es_primo_val = False
                break

        if es_primo_val:
            primos_encontrados.append(numero)
            contador_primos += 1

        numero += 1
        
    return f"Los primeros {N} números primos son: {', '.join(map(str, primos_encontrados))}"º