#Solicita al usuario su nombre, su apellido y su ciudad de nacimiento. Concaténalos en una sola cadena utilizando f-strings con el formato:
#"Hola, mi nombre es Nombre Apellido y nací en Ciudad."
#Imprime el resultado

nombre = input("Introduce tu nombre ")
apellidos = input("Introduce tus apellidos ")
c_nacimiento = input("Introduce tu ciudad de nacimiento ")

print (f"Hola, mi nombre es {nombre} {apellidos} y nací en {c_nacimiento}")