"""
    Algoritmo de busqueda ternaria usando un esquema iterativo
"""

def busqueda_ternaria(array, key, lo, n):
    while n >= 1:

        """ Obtenemos mid1 y mid2 """
        mid1 = lo + (n - lo)//3
        mid2 = n - (n - lo)//3

        # Chequeamos si el key esta en la mitad
        if key == array[mid1]:
            return mid1

        if key == array[mid2]:
            return mid2

        # Como no está presente en la mitad, se chequea
        # en que región esta presente y repetimos la busqueda
        if key < array[mid1]:
            n = mid1 - 1
        elif key > array[mid2]:
            lo = mid2 + 1
        else:
            lo = mid1 + 1
            n = mid2 - 1

    # key no encontrado
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # indice de partida
    l = 0

    # longitud del arreglo
    N = len(arr)

    # valor a buscar
    value = 8

    p = busqueda_ternaria(arr, value, l, N)

    print("El indice de {0} es {1}".format(value, p))
