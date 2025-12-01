from pathlib import Path

anyo = input("Introduce el año (ej: 2025): ")
mes_inicial_str = input("Introduce el mes inicial (1-12): ")
mes_final_str = input("Introduce el mes final (1-12): ")
num_dias_str = input("Introduce el número de días a crear por mes (ej: 5): ")

mes_inicial = int(mes_inicial_str)
mes_final = int(mes_final_str)
num_dias = int(num_dias_str)

for mes in range(mes_inicial, mes_final + 1):
    
    mes_str = str(mes).zfill(2)
    
    ruta_base_mes = Path("backups") / anyo / mes_str
    
    ruta_base_mes.mkdir(parents=True, exist_ok=True)
    
    for dia in range(1, num_dias + 1):
        
        dia_str = str(dia).zfill(2)
        
        nombre_dia = f"dia_{dia_str}"
        
        ruta_completa = ruta_base_mes / nombre_dia
        
        if ruta_completa.exists() and ruta_completa.is_dir():
            print("Carpeta existente (no creada): ", ruta_completa)
        else:
            ruta_completa.mkdir()
            print("Carpeta creada: ", ruta_completa)