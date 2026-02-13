with open("system_report.txt", "r") as f:
    leer = f.read()

with open("system_report_hisotry.txt", "a") as j:
    j.write("----------------------------------------------\n")
    j.write(f"{leer}\n")