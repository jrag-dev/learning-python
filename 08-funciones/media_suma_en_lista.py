"""
    Función que calcula la suma y la media en una lista
"""

def media(lista):
    total = 0
    for x in lista:
        total += x
    return total/(len(lista))


L = [1, 2, 3, 4, 5]
print(media(L))