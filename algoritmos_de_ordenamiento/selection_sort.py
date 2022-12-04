"""
    Implementación del algoritmo de clasificación por selección:

    Ordena un arreglo encontrando repetidamente el elemento minimo (considerando
    el order ascendente) de la parte no ordenada y colocándolo al principio.
"""


def swap(arr, xp, yp):
    temp = arr[xp]
    arr[xp] = arr[yp]
    arr[yp] = temp


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        swap(arr, i, min_idx)

    return arr


print(selection_sort([64, 25, 2, 7, 50, 99, 12, 22, 11]))
