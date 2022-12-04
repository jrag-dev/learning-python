"""
    Dado un arreglo array[] de N elementos, la tarea es escribir una función
    para buscar un elemento dado x en array[] usando el método de busqueda
    lineal.

    La busqueda lineal se define como un algoritmo secuencial que comienza
    en un extremo y recorre cada elemento de una lista hasta encontrar
    el elemento deseado; de lo contrario, la busqueda continua hasta el final
    del conjunto de datos. Es el algoritmo de busqueda mas sencillo, pero
    menos eficiente.

    Este algoritmo tiene complejidad temporal 0(N)
"""

def busqueda_lineal(array, value):
    for i, x in enumerate(array):
        if x == value:
            return i
    return -1


arr = [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
valor = 17

resultado = busqueda_lineal(arr, valor)

if resultado >= 0:
    print("El valor {0} se encuentra en la posición {1}".format(valor, resultado))
else:
    print("El valor {0} no se encuentra en el arreglo {1}".format(valor, arr))