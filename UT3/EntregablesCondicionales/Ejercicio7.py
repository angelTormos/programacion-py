from datetime import datetime

dia = datetime.now().weekday()

if dia == 5 or dia == 6:
    print("Ventana de mantenimiento")
else:
    print("Operación normal")