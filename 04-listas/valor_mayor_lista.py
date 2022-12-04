"""
    La lista de temperaturas de Mons, en Bélgica, fue almacenada en la lista
    L = [-10, -8, 0, 1, 2, 5, -2, -4]. Hacer un programa que imprima la temperatura
    menor y mayor, así como la temperatura media.
"""

L = [-10, -8, 0, 1, 2, 5, -2, -4]

maximo = L[0]
minimo = L[0]
suma = 0

for item in L:
    suma += item
    if item > maximo:
        maximo = item
    if item < minimo:
        minimo = item

media = suma/len(L)

print("Temperatura máxima: ", maximo)
print("Temperatura mínima: ", minimo)
print("Temperatura media: ", media)