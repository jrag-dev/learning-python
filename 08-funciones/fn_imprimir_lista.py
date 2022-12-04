"""
    Configuración de funciones con funciones
"""

def imprime_lista(lista, fimpresion, fcondicion):
    for x in lista:
        if fcondicion(x):
            fimpresion(x)

def imprime_elemento(x):
    print("Valor: %d" % x)

def espar(x):
    return x % 2 == 0

def esimpar(x):
    return not espar(x)


L = [1, 7, 9, 2, 11, 0, 8]

imprime_lista(L, imprime_elemento, espar)
imprime_lista(L, imprime_elemento, esimpar)