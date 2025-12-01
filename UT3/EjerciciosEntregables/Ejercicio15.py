from pathlib import Path

num_aulas = int(input("Introduce el número de aulas (A): "))
num_pcs = int(input("Introduce el número de PCs por aula (P): "))

total_general_logs = 0

for a in range(1, num_aulas + 1):
    
    nombre_aula = f"AULA-{a}"
    
    ruta_aula = Path(nombre_aula)
    
    total_logs_aula = 0
    
    for p in range(1, num_pcs + 1):
        
        nombre_pc = f"PC-{p}"
        
        ruta_pc = ruta_aula / nombre_pc
        
        if ruta_pc.is_dir():
            
            logs_en_pc = 0
            
            for archivo in ruta_pc.iterdir():
                
                if archivo.is_file() and archivo.suffix.lower() == '.log':
                    logs_en_pc += 1
            
            total_logs_aula += logs_en_pc
        
    print(f"Aula '{nombre_aula}': {total_logs_aula} archivos .log")
    
    total_general_logs += total_logs_aula

print(f"TOTAL GENERAL: {total_general_logs} archivos .log")
