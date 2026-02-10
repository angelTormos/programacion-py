from datetime import datetime

mensaje = input("Introduce un mensaje: ")

with open('admin_log.txt', 'a') as f:
    f.write(f"\n{datetime.now()} {mensaje}")