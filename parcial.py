
def cargar_producto(codigos, nombres, precios, stocks, contador):
    print("Cargando producto")
    code_valido = False
    
    
    while code_valido == False:
        codigo = int(input("Ingrese el codigo que desee ingresar: "))
        repetido = False
        for i in range(contador):
            if codigos[i] == codigo:
                repetido = True
                
        if repetido == True:
            print("Error: El producto ya esta cargador :p")
        else:
            code_valido = True  
            
    
    nombre = input("Ingrese el nombre de su producto: ")
    
    precio = float(input("Ingrese el Precio de su producto: "))
    while precio <= 0: 
        print("ERROR: precio invalido.. ")
        precio = float(input("ingrese el precio del producto: "))
    
    stock = int(input("Ingrese el stock de su producto: "))
    while stock < 0: 
        print("Error: el stock no puede ser negativo")
        stock = int(input("Ingrese el stock de su producto: "))
        
    
    codigos += [codigo]
    nombres += [nombre]
    precios += [precio]
    stocks += [stock]

    print("========================================")
    print(f"el producto {nombre} fue cargado con exito!")
    print("========================================")
    
    return contador + 1  

def mostrar_productos(codigos, nombres, precios, stocks, contador):
    print("Lista de Productos. ")
    if contador == 0:
        print("---------------------------------------")
        print("no hay productos registrados en el sistema. ")
        print("---------------------------------------")
    else:
        print("Codigo | Nombre | Precio | Stock")
        print("----------------------------")
        for i in range(contador):
            print(f"{codigos[i]} | {nombres[i]} | {precios[i]} | {stocks[i]}")
    

def buscar_producto_por_codigo(codigos, nombres, precios, stocks, contador):
    if contador == 0:
        print("no hay productos cargados en el sistema")
    else:
        buscado = int(input("ingrese el codigo a buscar: "))
        posicion = -1
        for i in range(contador):
            if codigos[i] == buscado:
                posicion = i
        if posicion != -1:
            print("======================")
            print("producto encontrado!")
            print("======================")
            print("-------")
            print(f"nombre. {nombres[posicion]}")
            print("-------")
            print(f"precio. {precios[posicion]}")
            print("-------")
            print(f"stock. {stocks[posicion]}")
            print("-------")
        else:
            print("ERROR: El codigo del producto que ingresaste no coincide con ninguno")

def ordenar_productos_men_precio(codigos, nombres, precios, stocks, contador):
    print("Ordenando productos por precio.. ")
    if contador < 2:
        print("no hay suficientes productos para ordenar.. ")
    else:
        for i in range(contador):
            for j in range(0, contador - i - 1):
                if precios[j] > precios[j + 1]:
                    aux_precio = precios[j]
                    precios[j] = precios[j + 1]
                    precios[j + 1] = aux_precio

                    aux_code = codigos[j]
                    codigos[j] = codigos[j + 1]
                    codigos[j + 1] = aux_code

                    aux_nombre = nombres[j]
                    nombres[j] = nombres[j + 1]
                    nombres[j + 1] = aux_nombre

                    aux_stock = stocks[j]
                    stocks[j] = stocks[j + 1]
                    stocks[j + 1] = aux_stock
        print("productos ordenados por precio..")

def mostrar_menor_stock(nombres, stock, contador):
    if contador == 0:
        print("no hay productos cargador...")
    else:
        pos_menor = 0
        for i in range(1, contador):
            if stock[i] < stock[pos_menor]:
                pos_menor = i
        print(f"el producto con menor cantidad disponible es {nombres[pos_menor]}")

def calcular_total_inventario(precios, stock, contador):
    if contador == 0:
        print("Inventario vacio: valor total : $0.0")
    else:
        total_acumulado = 0.0
        for i in range(contador):
            total_acumulado = total_acumulado + (precios[i] * stock[i])
        print(f"el Valor Total del inventario es: ${total_acumulado}.")

def menu():
    codigos = []
    nombres = []
    precios = []
    stocks = []
    contador_vueltas = 0
    while True:
        print("==============================")
        print("SUPERMERCADO PYTHON MARKET")
        print("==============================")
        print("1. Cargar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto por código")
        print("4. Ordenar productos por precio")
        print("5. Mostrar producto con menor stock")
        print("6. Calcular valor total del inventario")
        print("7. Salir")
        opcion = input("Ingrese La opcion que desee utilizar: ")
        if opcion == "1":
            contador_vueltas = cargar_producto(codigos, nombres, precios, stocks, contador_vueltas)
        elif opcion == "2":
            mostrar_productos(codigos, nombres, precios, stocks, contador_vueltas)
        elif opcion == "3":
            buscar_producto_por_codigo(codigos, nombres, precios, stocks, contador_vueltas)
        elif opcion == "4":
            ordenar_productos_men_precio(codigos, nombres, precios, stocks, contador_vueltas)
        elif opcion == "5":
            mostrar_menor_stock(nombres, stocks, contador_vueltas)
        elif opcion == "6":
            calcular_total_inventario(precios, stocks, contador_vueltas)
        elif opcion == "7":
            print("Chao nos vemos. ")
            break
        else:
            print("Numero invalo ingrese uno correcto. ")

menu()