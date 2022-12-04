"""
    Función que calcula la media en una lista
"""

def suma(lista):
    total = 0
    for x in lista:
        total += x
    return total

def media(lista):
    valor_media = suma(lista)/(len(lista))
    return valor_media


L = [1, 2, 3, 4, 5]

print(media(L))