from datetime import datetime

hora = datetime.now().hour

if hora < 12:
    print("Backup de mañana")
elif hora < 20:
    print("Backup de tarde")
else:
    print("Backup nocturno")