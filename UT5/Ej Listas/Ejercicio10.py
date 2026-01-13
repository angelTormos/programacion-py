lcompra = []
while True:
    print("\nGestión de Lista de la Compra") 
    print("1. Mostrar la lista") 
    print("2. Añadir elementos a la lista") 
    print("3. Borrar elementos de la lista") 
    print("4. Contar elementos de la lista") 
    print("5. Añadir una lista de elementos a la ya existente") 
    print("6. Borrar toda la lista") 
    print("7. Salir") 

    option = int(input("Introduce una opción: "))

    match option:
        case 1:
            if len(lcompra) == 0:
                print("La lista de la compra está vacia")
            else:
                print("La lista de la compra es:", ','.join(lcompra))
        case 2:
            producto = input("Introduce un producto a añadir")
            if producto not in lcompra:
                lcompra.append(producto)
            else:
                print("Este elemento ya existe")
        case 3:
            producto = input("Introduce el producto a eliminar")
            lcompra.remove(producto)
        case 4:
            print("Hay", len(lcompra), "productos en la lista")
        case 5:
            productos = input("Introduce los productos a añadir (separado por comas): ")
            prod2=productos.split(",")
            lcompra.extend(prod2)
        case 6:
            lcompra.clear()
        case 7:
            break