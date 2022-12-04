"""
    Implementación del algoritmo de busqueda de salto
"""
import math


def busqueda_de_salto(arr, key, n):

    """ Encontramos el tamaño del bloque a saltar"""
    step = int(math.sqrt(n))
    print(step)

    # Encontramos el bloque donde el elemento esta presente
    prev = 0
    while arr[int(min(step, n) - 1)] < key:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Se realiza la busqueda lineal
    while arr[int(prev)] < key:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == key:
        return int(prev)

    return -1


if __name__ == "__main__":
    array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    # longitud del arreglo
    N = len(array)

    # valor a buscar
    value = 55

    p = busqueda_de_salto(array, value, N)

    print("El indice de {0} es {1}".format(value, p))
