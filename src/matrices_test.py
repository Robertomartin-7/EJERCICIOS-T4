from matrices import suma_matrices, multiplica_matrices

def test_suma_matrices():
    # Caso de prueba 1: Suma de dos matrices 2x2
    m1 = [[1, 2],
          [3, 4]]
    m2 = [[5, 6],
          [7, 8]]
    resultado_esperado = [[6, 8],
                          [10, 12]]
    assert suma_matrices(m1, m2) == resultado_esperado

    # Caso de prueba 2: Suma de dos matrices 3x3
    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    m2 = [[9, 8, 7],
          [6, 5, 4],
          [3, 2, 1]]
    resultado_esperado = [[10, 10, 10],
                          [10, 10, 10],
                          [10, 10, 10]]
    assert suma_matrices(m1, m2) == resultado_esperado

    # Caso de prueba 3: Suma de matrices con dimensiones diferentes
    m1 = [[1, 2],
          [3, 4]]
    m2 = [[5, 6, 7],
          [8, 9, 10]]
    assert suma_matrices(m1, m2) == None

    # Caso de prueba 4: Suma de matrices con filas de diferente longitud
    m1 = [[1, 2],
          [3]]
    m2 = [[4, 5],
          [6, 7]]
    assert suma_matrices(m1, m2) == None

def test_multiplica_matrices():
    # Caso de prueba 1: Multiplicación de dos matrices 2x2
    m1 = [[1, 2],
          [3, 4]]
    m2 = [[5, 6],
          [7, 8]]
    resultado_esperado = [[19, 22],
                          [43, 50]]
    assert multiplica_matrices(m1, m2) == resultado_esperado

    # Caso de prueba 2: Multiplicación de una matriz 2x3 y una matriz 3x2
    m1 = [[1, 2, 3],
          [4, 5, 6]]
    m2 = [[7, 8],
          [9, 10],
          [11, 12]]
    resultado_esperado = [[58, 64],
                          [139, 154]]
    assert multiplica_matrices(m1, m2) == resultado_esperado

    # Caso de prueba 3: Multiplicación de una matriz por la identidad
    m1 = [[1, 2],
          [3, 4]]
    m2 = [[1, 0],
          [0, 1]]
    resultado_esperado = [[1, 2],
                          [3, 4]]
    assert multiplica_matrices(m1, m2) == resultado_esperado

    # Caso de prueba 4: Multiplicación de matrices con dimensiones incompatibles
    m1 = [[1, 2],
          [3, 4]]
    m2 = [[5, 6, 7]]
    assert multiplica_matrices(m1, m2) is None

    # Caso de prueba 5: Multiplicación de matrices con filas de diferente longitud
    m1 = [[1, 2],
          [3]]
    m2 = [[4, 5],
          [6, 7]]
    assert multiplica_matrices(m1, m2) is None

# Descomenta las llamadas de los tests que quieras ejecutar
test_suma_matrices()
#test_multiplica_matrices()
print("Todos los casos de prueba pasaron correctamente.")