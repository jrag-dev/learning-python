"""
    Busqueda lineal usando un enfoque recursivo
"""


def busqueda_lineal(arr, key, size):
    # Si el arreglo esta vacío se retorna -1
    if size == 0:
        return -1
    elif arr[size - 1] == key:
        return size - 1
    else:
        return busqueda_lineal(arr, key, size - 1)


if __name__ == "__main__":

    array = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    x = 110
    N = len(array)

    # Llamada a la función busqueda_lineal
    resultado = busqueda_lineal(array, x, N)
    if resultado == -1:
        print("El elemento no esta presente en el arreglo.")
    else:
        print("El elemento esta presente en el indice {0}".format(resultado))
