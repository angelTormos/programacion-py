from datetime import datetime
import platform
import os

with open("system_report.txt", "w") as f:
    f.write(f"{datetime.now()}\n")
    f.write(f"{platform.system()}\n")
    f.write(f"{os.cpu_count()}\n")