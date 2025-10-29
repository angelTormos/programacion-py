alumnos = int(input("Introduce el numero de almunos "))

if alumnos >= 100:
    t1 = alumnos * 65
    print("Se han de pagar 65 euros por alumno")
    print(f"Se pagará a la compañia {t1} €")
elif alumnos >= 50 and alumnos <= 99:
    t2 = alumnos * 70
    print("Se han de pagar 70 euros alumno")
    print(f"Se pagará a la compañia {t2} €")
elif alumnos >= 30 and alumnos <= 49:
    t3 = alumnos * 95
    print("Se han de pagar 95 euros alumno")
    print(f"Se pagará a la compañia {t3} €")
elif alumnos < 30:
    p = 2850/alumnos
    print(f"Se han de pagar {p}")