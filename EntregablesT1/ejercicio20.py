mon_2e = int(input("Número de monedas de 2€: "))
mon_1e = int(input("Número de monedas de 1€: "))
mon_50c = int(input("Número de monedas de 50 céntimos: "))
mon_20c = int(input("Número de monedas de 20 céntimos: "))
mon_10c = int(input("Número de monedas de 10 céntimos: "))

total = (mon_2e * 2) + (mon_1e * 1) + (mon_50c * 0.5) + (mon_20c * 0.2) + (mon_10c * 0.1)

print("Tienes un total de: ",total, "€")
