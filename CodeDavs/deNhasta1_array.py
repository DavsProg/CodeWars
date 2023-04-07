  """
    Esta función recibe un número entero positivo n 
    y devuelve una lista de enteros que 
    va desde n hasta 1 en orden descendente.
    """


def reverse_seq(n):
    lista_enteros = []
    for i in range(n, 0, -1):
        lista_enteros.append(i)
    return lista_enteros
