from datetime import datetime
fecha = datetime.now()

mensaje = input("Introduce un mensaje: ")

with open('log.txt', 'a') as f:
    f.write(f"{mensaje},{fecha}\n")