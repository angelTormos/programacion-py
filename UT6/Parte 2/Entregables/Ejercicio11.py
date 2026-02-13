from pathlib import Path

with open("daily_backup_list.txt", "a") as f:
    f.write("saludo.txt\n")
    f.write("numeros.txt\n")
    f.write("config.txt")

with open("daily_backup_list.txt", "r") as f:
    for linea in f:
        final = linea.strip()
        with open("backup_commands.txt", "a") as j:
            j.write(f"cp {final} /backup\n")