"""
    Programa para verificar si se encuentra un elemento en la lista
"""

L = [15, 7, 27, 39]

p = int(input("Digite el valor a buscar: "))

encontro = False
x = 0
while x < len(L):
    if L[x] == p:
        encontro = True
        break
    x += 1

if encontro:
    print("%d encontrado en la posición %d" % (p, x))
else:
    print("%d no encontrado" % p)