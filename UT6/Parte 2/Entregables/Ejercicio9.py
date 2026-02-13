from pathlib import Path

contador = 0

with open("cleanup_plan.txt", "w") as f:
    f.write("/tmp\n")
    f.write("/var/tmp\n")
    f.write("/noexiste")


with open("cleanup_plan.txt", 'r') as p:
    leer = p.readlines()
    print(leer)

for s in leer:
    i = Path(s.strip())
    print(i)
    contador = 0
    if i.exists() and i.is_dir():
        for _ in i.iterdir():
            contador += 1
        with open("cleanup_report.txt", "a") as j:
            j.write(f"{i} -> existe -> {contador}\n")
    else:
        with open("cleanup_report.txt", "a") as j:
            j.write(f"{i} -> NO existe\n")
