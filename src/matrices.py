def suma_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]:
    """
    Suma dos matrices y devuelve el resultado.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]]: Matriz resultante de la suma.
    """
    num_filas_m1 = len(m1)
    num_cols_m1 = len(m1[0])
    num_filas_m2 = len(m2)
    num_cols_m2 = len(m2[0])

    if not(num_filas_m1 == num_filas_m2 and num_cols_m1 == num_cols_m2):
        return None 

    if not(todas_filas_mismo_tam(m1) and todas_filas_mismo_tam(m2)):
        return None
    
    res = []
    for fila1, fila2 in zip(m1, m2):
        fila = []
        for e1, e2 in zip(fila1, fila2):
            fila.append(e1 + e2)
        res.append(fila)
    return res

    # TODO: Hacer con range en lugar de zip
    #for i in range(num_filas_m1): #indice de filas
        #for j in range(num_cols_m1): # indice de columnas

def todas_filas_mismo_tam(m:list[list[int | float]]) -> bool:
    if len(m)==0:
        return True
    
    todas_mismo_tam = True
    tam = len(fila[0])
    for fila in m:
        if len(fila) != tam:
            todas_mismo_tam = False
            break
    return todas_mismo_tam

def multiplica_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]:
    """
    Multiplica dos matrices y devuelve el resultado.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]]: Matriz resultante de la multiplicación.
    """
    if len(m1) == 0 or len(m2) == 0:
        return None
    
    if not (todas_filas_mismo_tam(m1) and todas_filas_mismo_tam(m2)):
        return None
    
    num_filas_m1 = len(m1)
    num_columnas_m1 = len(m1[0])
    num_filas_m2 = len(m2)
    num_columnas_m2 = len(m2[0])

    if num_columnas_m1 != num_filas_m2:
        return None
    
    res = inicializa_matriz(num_filas_m1, num_columnas_m2)
    num_filas_res = num_filas_m1
    num_columnas_res = num_columnas_m2

    for i in range(num_filas_res):
        for j in range(num_columnas_res):
            for k in range(num_columnas_m1):
                res[i][j] += m1[i][k] * m2[k][j]
    
    return res

def inicializa_matriz(num_filas: int, num_columnas: int) -> list[list[int|float]]:
    res = [0]
    for i in range(num_filas):
        fila = [0] * num_columnas
        res.append(fila)
    return res

