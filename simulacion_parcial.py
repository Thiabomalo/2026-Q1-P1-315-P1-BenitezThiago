bibloteca = [
    [["Titulo: Python basico.", "autor: Ana Lopez", "anio: 2024"], [1]],
    [["El Principito", "autor : Antoine de Saint-Exupéry", "anio : 1943"], [5]],
    [["Titulo: Rayuela", "autor: Julio Cortazar", "anio: 1963"], [3]],
    [["Titulo: Fundacion", "autor: Isaac Asimov", "anio: 1951"], [7]]
]
def mostar_bibloteca(lista_libros):
    print("========BIBLOTECA=======")
    for libro in lista_libros:
        datos = libro[0]
        cantidad = libro[1]
        print("LIBROS:")
        print("TITULO- " + str(datos[0]))
        print("AUTOR " + str(datos[1]))
        print("AÑO- " + str(datos[2]))
        print("Stock: " + str(cantidad[0]) + " Unidades")
        print("-" * 28)

def agregar_libro(lista_libros):
    continuar = "si"
    while continuar != "salir":
        print("-Ingreso de nuevo libro")
        titulo = input("titulo: ")
        autor = input("Autor: ")
        anio = int(input("Año: "))
        cantidad = int(input("Cantidad: "))
        datos_nuevo = [titulo, autor, anio]
        nuevo_cantidad = [cantidad]
        nuevo_item = [datos_nuevo, nuevo_cantidad]
        lista_libros = lista_libros + [nuevo_item]
        print("cargado con exito uwu")
        continuar = input("Desea continuar (salir para terminar)")
    return lista_libros
def buscar_libro(lista_libros):
    busqueda = input("ingrese el titulo exacto a buscar: ")
    for libro in lista_libros:
        if libro[0][0] == busqueda:
            print("encontrado! stock actual es " + str(libro[1][0]))
            break
    else:
        print("no se encontro el libro :,v")
def prestar_libros (lista_libros):
    prestar = input("Que libros queres llevartEe?: ")
    for libros in lista_libros:
        if libros[0][0] == prestar:
            if libros[1][0] > 0:
                libros[1][0] = libros[1][0] - 1
                print("Te lukeaste el libro quedan: " + str(libros[1][0]))
            else:
                print("no hay stok flaco :(")
def devolver_libro(lista_libros):
    devolver = input("Que libro queres devolver? ")
    for libro in lista_libros:
        if libro[0][0] == devolver:
            libro[1][0] = libro[1][0] + 1
            print("Libro devuelto uwu " + str(libro[1][0]))
            break
    else:
        print("sin stock :c")

def libros_agotados(lista_libros):
    print("libros agotados")
    agotados = False
    for libros in lista_libros:
        if libros[1][0] == 0:
            print("libros agotado :c" + libros[0][0])
            agotados = True
    if agotados == False:
        print("por ahora stock full sin agotados nwn")
def menu(lista_libros):
    while True:
        print("Bienvenido que opcion desea ingresar")
        print("1. agregar libro")
        print("2. mostrar todos los libro")
        print("3. buscar libro x titulo")
        print("4. prestar libro")
        print("5. devolver libro")
        print("6. Mostrar Libros sin stock")
        print("7. salir")
        opcion = input("Ingrese la opcion que desea ver: ")
        if opcion == "1":
            print("hora de cargar un nuevo libro nwn")
            lista_libros = agregar_libro(lista_libros)
        elif opcion == "2":
            mostar_bibloteca(lista_libros)
        elif opcion == "3":
            buscar_libro(lista_libros)
            print("")
        elif opcion == "4":
            prestar_libros(lista_libros)
        elif opcion == "5":
            devolver_libro(lista_libros)
        elif opcion == "6":
            libros_agotados(lista_libros)
        elif opcion == "7":
            print("NOS VEMOS CTM")
            break
        else:
            print("opcion incorrecta intentelo otra vez")
menu(bibloteca)