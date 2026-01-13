nombre = ""
edad = 0
lnombre = []
ledad = []
nombre = input("Introduce el nombre: ")

while nombre != "*":
    edad = int(input("Introduce la edad: "))
    lnombre.append(nombre)
    ledad.append(edad)
    nombre = input("Introduce el nombre: ")

for i in range(len(ledad)):
    if ledad[i] >= 18:
        print(lnombre[i], ledad[i])

m_edad = max(ledad)
for i in range(len(ledad)):
    if ledad[i] == m_edad:
        print(lnombre[i])