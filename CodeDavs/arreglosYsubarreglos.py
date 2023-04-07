
"""
La función find_subarray_with_same_element recibe dos argumentos: una lista de enteros positivos a y un número entero positivo k.

Primero, verifica si k está presente en a. Si no, devuelve (-1, -1).

Si k está en a, la función inicializa las variables start, end, longest y current a 0. start y end representan los índices de inicio y final de la sublista más larga de elementos iguales a k. longest representa la longitud de la sublista más larga y current representa la longitud actual de la sublista de elementos iguales a k que se está explorando.

Luego, la función recorre la lista a y, si el elemento actual es igual a k, aumenta current en 1. Si current es mayor que longest, actualiza longest y actualiza start y end con los índices de inicio y final de la sublista más larga de elementos iguales a k.

Si el elemento actual no es igual a k, la función restablece current a 0.

Finalmente, la función devuelve start y end como una tupla en el formato (inicio, fin).

"""
def find_subarray_with_same_element(a, k):
    if k not in a:   # Si el número k no está en la lista a
        return (-1, -1)   # devuelve el resultado (-1, -1)

    start, end = 0, 0   # Inicializa los valores de inicio y fin de sublista en 0
    longest = 0   # Inicializa la longitud máxima de sublista en 0
    current = 0   # Inicializa la longitud actual de sublista en 0

    for i, x in enumerate(a):   # Recorre la lista a con un índice i y un valor x en cada iteración
        if x == k:   # Si el valor x es igual al número k
            current += 1   # aumenta la longitud actual de sublista en 1
            if current > longest:   # Si la longitud actual de sublista es mayor que la longitud máxima de sublista
                longest = current   # actualiza la longitud máxima de sublista a la longitud actual de sublista
                start, end = i - longest + 1, i   # actualiza los valores de inicio y fin de sublista

        else:   # Si el valor x no es igual al número k
            current = 0   # restablece la longitud actual de sublista a 0

    return (start, end)   # devuelve el resultado (inicio, fin) de la sublista más larga


"""
Test con los parámetros a = [2, 1, 1, 1, 1, 3, 3, 4, 5, 1, 1, 1] y k = 3. El resultado esperado es (5, 6), que indica que el subarreglo más largo que consiste solo en el número 3 comienza en la posición 5 y termina en la posición 6.

Test con los parámetros a = [2, 1, 1, 1, 1, 3, 3, 4, 5, 1, 1, 1, 1] y k = 1. En este caso, hay dos subarreglos que consisten solo en el número 1 y ambos tienen la misma longitud, pero se espera que se devuelvan los índices del último de estos subarreglos, es decir, (9, 12).

Test con los parámetros a = [1, 2, 3] y k = 9. Como el número 9 no está presente en el arreglo a, se espera que se devuelva (-1, -1).

Test con los parámetros a = [1] y k = 1. Dado que el arreglo a tiene solo un elemento que es igual a 1, se espera que se devuelva (0, 0).

Test con los parámetros a = [1, 2, 3] y k = 4. Como el número 4 no está presente en el arreglo a, se espera que se devuelva (-1, -1)
"""
