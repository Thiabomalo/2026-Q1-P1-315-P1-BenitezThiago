
def insertar_elemento(lista, elemento, posicion=None):
    if posicion == None:
        posicion = len(lista) # Si no se define, va al final
        
    #Agrandamos la lista un espacio agregando un casillero vacío al final
    lista += [None] 
    
    #Desplazamos los elementos hacia la derecha (empezando desde el final)
    #    para abrir el "hueco" en la posición que queremos.
    for i in range(len(lista) - 1, posicion, -1):
        lista[i] = lista[i - 1]
        
    # 3. Ponemos el nuevo elemento en el hueco que liberamos
    lista[posicion] = elemento
    
    print(f"Elemento '{elemento}' insertado en el índice {posicion}.")
    return lista


def recorrer_lista(lista):
    print("Recorriendo la lista:")

    for i in range(len(lista)):
        print(f"  Índice {i} -> Valor: {lista[i]}")
    print("-" * 20)

def eliminar_elemento(lista, elemento):
    posicion_encontrada = -1
    
    # Buscamos manualmente el índice del elemento
    for i in range(len(lista)):
        if lista[i] == elemento:
            posicion_encontrada = i
            break 
            
# Si no se encontró, devolvemos la lista intacta
    if posicion_encontrada == -1:
        print(f"Error: El elemento '{elemento}' no se encuentra en la lista.")
        return lista

    
    lista_nueva = [0] * (len(lista) - 1)
    
    
    indice_nuevo = 0
    for i in range(len(lista)):
        if i != posicion_encontrada:
            lista_nueva[indice_nuevo] = lista[i]
            indice_nuevo = indice_nuevo + 1 # Avanzamos al siguiente casillero
            
    print(f"Elemento '{elemento}' eliminado exitosamente.")
    return lista_nueva


def buscar_elemento(lista, elemento):
    # Recorremos la lista comparando uno por uno
    for i in range(len(lista)):
        if lista[i] == elemento:
            print(f"Búsqueda: El elemento '{elemento}' está en el índice {i}.")
            return i  #Retorna el indice apenas lo encuentra
            
    print(f"Búsqueda: El elemento '{elemento}' NO está en la lista.")
    return -1



#EJEMPLO DE USO DE LAS FUNCIONES


mi_lista = ["Manzana", "Banana", "Naranja"]
print(f"Lista inicial: {mi_lista}")

#Recorre
recorrer_lista(mi_lista)

#Inserta
insertar_elemento(mi_lista, "Uva")             # Al final (índice 3)
insertar_elemento(mi_lista, "Pera", 1)         # En medio (índice 1)
print(f"Lista actual: {mi_lista}\n")

#Busca
buscar_elemento(mi_lista, "Banana")
buscar_elemento(mi_lista, "Sandía")            
print()

#Elimina
eliminar_elemento(mi_lista, "Manzana")
print(f"Lista final: {mi_lista}")