"""
    Dada una matriz ordenada array[] de n elementos, escribir una función para
    buscar un elemento dado x en array[] y devuelve el indice en la matriz.
"""

def busqueda_binaria(array, value):
    lo = 0
    hi = len(array) - 1

    while hi - lo > 1:
        mid = (hi + lo)//2
        if array[mid] < value:
            print(lo, hi)
            lo = mid + 1
        else:
            hi = mid
            print(lo, hi)

    if array[lo] == value:
        return lo
    elif array[hi] == value:
        return hi
    else:
        return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 60, 110, 120, 130, 170]
    valor = 30
    N = len(arr)

    resultado = busqueda_binaria(arr, valor)

    print(resultado)