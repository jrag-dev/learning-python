"""
    Pasar parámetros empaquetados en una lista.
"""


def suma(a, b):
    print(a + b)


L = [2, 3]
suma(*L)
# el * indica que queremos desenpaquetar la lista L para usar sus
# valores como parámetro para la función suma.


def barra(n=10, c="*"):
    print(c*n)


L = [[5, "-"], [10, "*"], [5], [6, "."]]

for x in L:
    barra(*x)