from pathlib import Path

with open('commands.txt', 'w') as f:
    f.write("ls -la, df -h, uname -a")

archivo = Path('commands.txt')

leer_archivo = archivo.read_text()

with open('commands_numbered.txt', 'w') as j:
    for line_no, line in enumerate(leer_archivo.strip().split(",")):
        j.write(f"{line_no}: {line}\n")
