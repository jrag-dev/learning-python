"""
    Mostrar indices usando la función enumerate
    
    La función enumerate genera una tupla en la cual el primer valor
    es el índice y el segundo es el elemento de la lista enumerada.
"""

L = [4, 5, 7, 9, 12]

for x, item in enumerate(L):
    print("[%d] %d" % (x, item))