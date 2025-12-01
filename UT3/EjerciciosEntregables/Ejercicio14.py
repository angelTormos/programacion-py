from pathlib import Path

anyo = input("Introduce el año (ej: 2025): ")
mes_inicial = int(input("Introduce el mes inicial (1-12): "))
mes_final = int(input("Introduce el mes final (1-12): "))
num_dias = int(input("Introduce el número de días a crear por mes (ej: 5): "))

for mes in range(mes_inicial, mes_final + 1):
    if mes < 10:
        mes_str = "0" + str(mes)
    else:
        mes_str = str(mes)
    
    ruta_base_mes = Path("backups") / anyo / mes_str
    ruta_base_mes.mkdir(parents=True, exist_ok=True)
    
    for dia in range(1, num_dias + 1):
        if dia < 10:
            dia_str = "0" + str(dia)
        else:
            dia_str = str(dia)
        
        nombre_dia = f"dia_{dia_str}"
        ruta_completa = ruta_base_mes / nombre_dia
        
        if ruta_completa.exists() and ruta_completa.is_dir():
            print("Carpeta existente (no creada): ", ruta_completa)
        else:
            ruta_completa.mkdir()
            print("Carpeta creada: ", ruta_completa)