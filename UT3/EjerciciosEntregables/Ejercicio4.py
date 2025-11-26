from datetime import datetime, timedelta
import os

fecha = datetime.now().date()

for _ in range(8):
    nombre = f"backup_{fecha.strftime("%Y_%m_%d")}.zip"
    print(nombre)
    fecha = fecha + timedelta(days=1)