# FP1 - Teoría - Ejercicios del Tema 4

## Ejercicio 1: Lista de nombres ordenada por longitud

Queremos trabajar con listas de nombres que se mantengan siempre ordenadas por longitud de los nombres. Para ello, implementa una función `inserta_ordenado` en el módulo `listas.py` que reciba una lista y un nuevo nombre y lo inserte en la posición adecuada. Supondremos que la lista recibida está previamente ordenada según el criterio especificado. 

Antes de llevar a cabo el algoritmo de inserción en orden, la función comprobará que la lista recibida esté correctamente ordenada. Si no lo estuviera, la función no hará nada (la lista recibida no es modificada).

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`. 

## Ejercicio 2: Buscar duplicados

Implementa una función `busca_duplicados` en el módulo `listas.py` que reciba una lista y devuelva otra lista con los elementos de la primera que aparecen más de una vez. 

Intenta implementarlo de dos formas:
1. Usando el método `count`. 
2. Usando *slicing* y sin usar el método `count`

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`.

## Ejercicio 3: Generador de listas aleatorios sin repeticiones consecutivas

Implementa una función `genera_aleatorios` que genere una lista de números enteros aleatorios, sin que haya dos elementos consecutivos que sean iguales.  La función permite indicar mediante parámetros el rango en el que se generan los números aleatorios, y el tamaño de la lista a generar. 

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`. 

## Ejercicio 4: Intercala listas

Implementa una función `intercala_listas` que reciba dos listas y devuelva una nueva lista intercalando los elementos de las listas recibidas: primero un elemento de la primera, luego un elemento de la segunda, luego un elemento de la primera, etc. Si una de las listas tiene más elementos que la otra, se introducirán todos los elementos sobrantes tal cual en la lista resultante.

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`. 

## Ejercicio 5: Mezcla listas ordenadas

Implementa una función `mezcla_ordenadas` que reciba dos listas ordenadas y devuelva una nueva lista también ordenada con todos los elementos de ambas listas. Si una de las listas tiene más elementos que la otra, se introducirán todos los elementos sobrantes tal cual en la lista resultante.

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`. 

## Ejercicio 6: Ordenación *Bubble Sort*

El método de ordenación *Bubble Sort* no es el método más eficiente para ordenar una lista, pero es relativamente sencillo de implementar. El algoritmo es el siguiente:

1. Recorre la lista comparando elementos adyacentes.
2. Si un par de elementos está en el orden incorrecto, se intercambian.
3. Se repite el proceso hasta que no se realicen más intercambios en una pasada completa.

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`.

## Ejercicio 7: Suma de matrices

Implementa una función `suma_matrices` en el módulo `matrices.py` que reciba dos matrices numéricas de las mismas dimensiones y devuelva el resultado de sumar ambas.

Antes de llevar a cabo el algoritmo de suma, la función comprobará si se cumplen las siguientes condiciones:
* Todas las filas de cada matriz recibida tienen exactamente el mismo número de elementos.
* El número de columnas y filas de ambas matrices es el mismo.

Si no se cumple alguna de las condiciones anteriores, la función debe devolver `None`. 

Ejecuta las pruebas del módulo `matrices_test.py`y asegúrate de que se pasan todas correctamente.

## Ejercicio 8: Multiplicación de matrices

Implementa una función `multiplica_matrices` en el módulo `matrices.py` que reciba dos matrices de números y devuelva el resultado de multiplicar ambas. 

Antes de llevar a cabo el algoritmo de multiplicación, la función comprobará si se cumplen las siguientes condiciones:
* Todas las filas de cada matriz recibida tienen exactamente el mismo número de elementos.
* El número de columnas de la primera matriz coincide con el número de filas de la segunda matriz.

Si no se cumple alguna de las condiciones anteriores, la función debe devolver `None`. 

Para llevar a cabo el algoritmo de multiplicación, comienza creando una matriz resultado del tamaño esperado, rellena de ceros. 

Ejecuta las pruebas del módulo `matrices_test.py`y asegúrate de que se pasan todas correctamente.

## Ejercicio 9: Datos de películas

Disponemos de datos sobre películas en un fichero con formato CSV (*Comma-Separated Values*), ubicado en `data/peliculas.csv`. Python dispone de un módulo `csv` con utilidades para leer este tipo de archivos. Queremos implementar una serie de funciones en el módulo `peliculas.py` para leer los datos del fichero y contestar a ciertas preguntas sobre las películas. Cada película estará representada por una tupla nombrada `Pelicula`, que ya está definida en `peliculas.py`. 

### Función `lee_peliculas`

Se te proporciona parte de la implementación de `lee_peliculas`:
* Ejecuta con ayuda del depurador una llamada a esta función, y observa cómo funciona la lectura del CSV.
* Modifica el `for` para que use una variable por cada campo del CSV mediante *unpacking*.
* Implementa el código dentro del `for` para que se construya una tupla de tipo `Pelicula` con los valores de las variables del `for`. Asegúrate de que cada valor sea del tipo adecuado
* La función debe acumular todas las tuplas creadas en una lista, y finalmente devolverla.

Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `existe_pelicula`

Devuelve `True` si existe alguna película cuyo titulo contiene una determinada cadena, y `False` en caso contrario. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `son_todas_director_genero`

Devuelve `True` si todas las películas de un director dado contienen el genero indicado en su lista de géneros, y `False` en caso contrario. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `construye_lista_titulos_actor`

Devuelve una lista de títulos en los que el actor indicado aparece en el reparto. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `calcula_presupuesto_total_año`

Suma y devuelve el presupuesto total de las películas cuyo año de estreno es el indicado. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `encuentra_pelicula_mayor_recaudacion`

Devuelve la película con mayor recaudacion entre las que incluyen el genero dado. Si no existe ninguna de ese género, devuelve `None`. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.
