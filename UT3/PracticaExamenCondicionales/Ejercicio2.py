from datetime import datetime

fecha = datetime.now().hour

if fecha < 12:
    print("Backup mañana")
elif fecha > 12 and fecha < 20:
    print("Backup tarde")
else:
    print("Backup noche")