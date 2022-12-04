"""
    Busqueda binaria implementada de forma recursiva
"""

def busqueda_binaria(array, lo, hi, value):

    # Chequeamos el caso base:
    if hi >= 1:
        mid = lo + (hi - 1)//2

        # Si el elemento esta presente en la mitad, lo devolvemos
        if array[mid] == value:
            return mid

        # Si el elemento es menor que la mitad, entonces, este sólo
        # puede estar presente en el subarreglo de la izquierda
        elif array[mid] > value:
            return busqueda_binaria(array, lo, mid - 1, value)

        # Sino el elemento sólo puede estar en el subarreglo
        # de la derecha
        else:
            return busqueda_binaria(array, mid + 1, hi, value)

    # Si hi < 1 entonces no se encuentra el valor buscado
    else:
        return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr) - 1

    resultado = busqueda_binaria(arr, 0, N, x)

    if resultado != -1:
        print("Elemento encontrado en la posición {0}".format(resultado))
    else:
        print("Elemento no encontrado en el arreglo.")