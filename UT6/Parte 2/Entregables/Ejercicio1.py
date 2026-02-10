from datetime import datetime
import platform
import os


fecha = datetime.now()
sistema = platform.system()
cpu = os.cpu_count()


with open('system_report.txt', 'w') as f:
    f.write(f'La fecha y hora de hoy es {fecha}\nEl sistema operativo es {sistema}\nY tienes {cpu} CPUs')