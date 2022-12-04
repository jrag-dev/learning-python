"""
    Realizar un programa para investigar si un elemento está o no en una lista,
    verificando si el valor buscado está presente desde el primero al último elemento.
"""

L = [4, 8, 11, 3, 5, 9, 21]

elemento = int(input("Digite el valor a buscar: "))

encontro = False
i = 0
while i < len(L):
    if L[i] == elemento:
        encontro = True
        break
    i += 1

if encontro:
    print("%d encontrado en la posición %d" % (elemento, i))
else:
    print("%d no encontrado en la lista" % elemento)