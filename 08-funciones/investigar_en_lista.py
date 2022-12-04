"""
    Funcion que recibe una lista y un valor a buscar en la lista
"""

def investigar(lista, valor):
    for i, x in enumerate(lista):
        print("{0}: {1:<10}".format(i, x))
        if x == valor:
            return i, x
    return None, valor


lugar, numero = investigar([5, 8, 10, 9, 22], 10)

if lugar is None or numero is None:
    print("{} no se encuentra en la lista".format(numero))
else:
    print("{0} se encuentra en la posición {1}".format(numero, lugar))