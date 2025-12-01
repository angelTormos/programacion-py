while True:
    contrasena = input("Introduce una contraseña: ")
    
    if len(contrasena) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        continue
        
    tiene_digito = False
    
    for caracter in contrasena:
        if caracter.isdigit():
            tiene_digito = True
            break
    
    if not tiene_digito:
        print("La contraseña debe contener al menos un dígito.")
        continue
        
    print("Contraseña validada con éxito.")
    break