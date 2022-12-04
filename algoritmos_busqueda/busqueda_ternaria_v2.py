"""
    Implementación del algoritmo de busqueda ternaria. Este es un algoritmo que se puede usar
    para encontrar un elemento en un arreglo. Es similar a la busqueda binaria donde dividimos
    el arreglo en dos partes, pero en este algoritmo, dividimos el arreglo dado en tres
    partes y determinamos cuál tiene la clave (elemento buscado).

    Se divide el arreglo en tres partes tomando mid1 y mid2, que se pueden calcular como:
    mid1 = lo + (rl)/3
    mid2 = r - (rl)/3

    Inicialmente, lo y r serán iguales a 0 y n-1 respectivamente, donde n es la longitud
    del arreglo.

    El arreglo debe estar ordenado para poder aplicar la busqueda.
"""


def busqueda_ternaria(array, lo, r, key):
    if r >= 1:
        # Obtener mid1 y mid2
        mid1 = lo + (r - lo) // 3
        mid2 = lo + (r - lo) // 3

        # Chequear si key esta presente en alguna de las mitades
        if array[mid1] == key:
            return mid1

        if array[mid2] == key:
            return mid2

        # Chequear en que región esta presente y
        # repetir las operaciones de busqueda en esta región
        if key < array[mid1]:
            return busqueda_ternaria(array, lo, mid1 - 1, key)

        elif key > array[mid2]:
            return busqueda_ternaria(array, mid2 + 1, r, key)

        else:
            return busqueda_ternaria(array, mid1 + 1, mid2 - 1, key)

    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # indice de partida
    l = 0

    # longitud del arreglo
    N = len(arr)

    # valor a buscar
    value = 8

    p = busqueda_ternaria(arr, l, N, value)

    print("El indice de {0} es {1}".format(value, p))
