"""
    Implementación del algoritmo de clasificación por burbujas:
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            print(i, j)
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
    return arr


array = bubble_sort([64, 25, 2, 7, 50, 99, 12, 22, 11])
print(array)