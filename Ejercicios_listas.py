import random as r
"""
Ejercicio 1
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo
"""

def inicializar_lista():
    lista_creada_y_vacia = [0] * 10
    print(f"lista creada uwu")
    return lista_creada_y_vacia




def rellenar_lista(lista:list):
    for i in range(len(lista)):
        lista[i] = r.randint(1,10)
    print("lista llenada con num aleatorios del 1 al 10")
    return lista

def imprimir_potencias(lista:list):
    print("VALOR | CUADRADO | CUBO ")
    print("------------------------")
    for num in lista:
        cuadrado = num ** 2
        cubo = num ** 3
        print(f"{num} | {cuadrado} | {cubo}")



def menu():
    creada = False
    relleada_flag = False
    lista = []
    print("Bienvenido al progamaa super epico de thiabomaLO")
    while True:
        print("------------")
        print("1 - inicializar la lista (con 0)")
        print("2 - rellenar la lista con numeros randoms..")
        print("3 - printear la lista con su numero correspondiente/cuadrado/cubo")
        print("4 - printear la lista xqsy ")
        print("0 - salir chau nos vimos")
        opcion = input("Seleccione una opcion 1/2/3/4/0: ")
        if opcion == "1":
            print("lista creada pa")
            lista = inicializar_lista()
            creada = True
        elif opcion == "2":
            if creada == True:
                rellena = rellenar_lista(lista)
                relleada_flag = True
            else:
                print("No pasare por opcion 1 bo")
        elif opcion == "3":
            if creada == True and relleada_flag == True:
                imprimir_potencias(rellena)
            else:
                print("no pasaste por opcino 1 o por opcion 2")
        elif opcion == "4":
            if creada == True:
                elegir = input("deseas ver la lista rellena o la vacia?: LLENA/VACIA ")
                if elegir.lower() == "llena" and relleada_flag == True:
                    print(rellena)
                elif elegir.lower() == "vacia":
                    print(lista)
                else:
                    print("opcion incorrecta")
            else:
                print("falta pasar por opcion 1 o 2 o 3 o 4 o5 o6 o7 o 8 o 9 o10 ")
        elif opcion == "0":
            print("nos vemos chau")
            break



"""
Ejercicio 2
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
"""
def crear_lista_e_iniciarlizarla()-> list:
    lista_crear = input("deseas crear una lista?: ")
    if lista_crear.lower() == "si":
        print("Lista creada chaval")
        print("cargando...")
        print("cargando...")
        print("cargando...")
        print("cargando...")
        print("cargando...")
        print("cargando...")
        print("cargando...")
        print("cargando...")
        lista = [0] * 5
        for i in range(len(lista)):
            llenar = input(f"ingresa {i + 1 } con que deseas llenar la lista")
            lista[i] = llenar
    return lista

def dar_vuelta_lista(lista:list):
    lista_invertida = lista[:: - 1 ]
    
    print("lista normal")
    print (lista)
    print("lista invertida")
    print (lista_invertida)

    
