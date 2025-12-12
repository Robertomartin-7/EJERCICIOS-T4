import random

def inserta_ordenado(lista_nombres: list[str], nombre: str) -> None:
    """
    Inserta un nombre en una lista de nombres manteniendo el orden (de menor a mayor longitud).
    Si la lista recibida no estuviera ordenada por longitud, la función no hace nada.

    Parámetros:
    lista_nombres (list[str]): Lista de nombres ordenada por longitud.
    nombre (str): Nombre a insertar.
    """
    # Comprobar que lista_nombres está ordenado por longitud
    # ["ana", "maría", "miguelángel", ...]
    ordenada = True
    for n1, n2 in zip(lista_nombres, lista_nombres[1:]):
        if len(n1) > len(n2):
            ordenada = False
            break
    
    if not ordenada:
        return # Igual que poner return None

    posicion_a_insertar = None
    for i, elem in enumerate(lista_nombres):
        if len(elem) > len(nombre):   # se podría usar >=
            # Esta es la posición donde debería ir nombre
            posicion_a_insertar = i
            break
    
    if posicion_a_insertar != None:
        lista_nombres.insert(posicion_a_insertar, nombre)
    else:
        lista_nombres.append(nombre)

def busca_duplicados(lista: list) -> list:
    """
    Busca y devuelve una lista con los elementos duplicados en la lista recibida.

    Parámetros:
    lista (list): Lista en la que buscar duplicados.

    Devuelve:
    list: Lista con los elementos duplicados.
    """
    #MÉTODO COUNT
    res = []
    for elem in lista:
        if lista.count(elem) > 1 and elem not in res:
            res.append(elem)
    return res

    #SLICING
    res = []
    for elem1, elem2 in zip(lista, lista[1:]):
        if elem1 == elem2 and elem1 not in res and elem2 not in res:
            res.append(elem1)
    return res

def genera_aleatorios(n: int, minimo: int, maximo: int) -> list[int]:
    """
    Genera una lista con n números enteros aleatorios en un rango dado,
    asegurando que no haya dos elementos consecutivos iguales.

    Parámetros:
    n (int): Número de elementos en la lista.
    minimo (int): Valor mínimo del rango (inclusive).
    maximo (int): Valor máximo del rango (inclusive).

    Devuelve:
    list[int]: Lista con n números enteros aleatorios.
    """
    lista_resultado = []
    if n == 0:
        return lista_resultado
    numero_aleatorio = random.randint(minimo, maximo)
    lista_resultado.append(numero_aleatorio)
    for i in range(1, n):
        numero_aleatorio = random.randint(minimo, maximo)
        while numero_aleatorio == lista_resultado[-1]:
            numero_aleatorio = random.randint(minimo, maximo)
        lista_resultado.append(numero_aleatorio)
    
    return lista_resultado

def intercala_listas(lista1: list, lista2: list) -> list:
    """
    Intercala dos listas. Si una lista es mayor que la otra, 
    los elementos sobrantes se añaden al final.

    Parámetros:
    lista1 (list): Primera lista.
    lista2 (list): Segunda lista.

    Devuelve:
    list: Lista resultante de intercalar las dos listas.
    """
    res = []
    for a, b in zip(lista1, lista2):
        res.append(a)
        res.append(b)
    if len(lista1) > len(lista2):
        res.extend(lista1[len(lista2):])
    elif len(lista2) > len(lista1):
        res.extend(lista2[len(lista1):])
    return res

def mezcla_ordenadas(lista1: list, lista2: list) -> list:
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    lista1 (list): Primera lista ordenada.
    lista2 (list): Segunda lista ordenada.

    Devuelve:
    list: Lista resultante de mezclar las dos listas ordenadas.
    """
    '''i, j = 0, 0
    res=[]
    while i<len(lista1) and j<len(lista2):
        if lista1[i]<lista2[j]:
            res.append(lista1[i])
            i+=1
        else:
            res.append(lista2[j])
            j+=1
    
    if i==len(lista1):
        res.extend(lista2[j:])
    #elif j==len(lista2): 
    else:
        res.extend(lista1[i:])
    return res'''

    res = []
    if not lista1 and not lista2:
        return res
    elif not lista1:
        return lista2
    elif not lista2:
        return lista1

    copia1 = lista1.copy()
    copia2 = lista2.copy()

    while copia1 and copia2:
        if copia1[0] <= copia2[0]:
            res.append(copia1.pop(0))
        else:
            res.append(copia2.pop(0))

    if copia1:
        res.extend(copia1)
    elif copia2:
        res.extend(copia2)
            
    return res

def ordena_bubble_sort(lista: list) -> None:
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento bubble sort. 

    Parámetros:
    lista (list[int]): Lista de números enteros a ordenar.
    """
    ha_cambiado = True 
    while ha_cambiado:   
        ha_cambiado = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ha_cambiado = True

    # TODO RETO: Medir el tiempo de ejecución para varias listas (grandes)
    # para tratar de estimar la complejidad (cuánto tarda en ejecutarse
    # en función del tamaño de la lista)