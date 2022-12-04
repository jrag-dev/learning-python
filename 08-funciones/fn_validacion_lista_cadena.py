"""
    Escriba una función que reciba una cadena de caracteres y una lista. La función
    debe comparar la cadena de caracteres pasada con los elementos de la lista,
    también pasada como parámetro. Retorne verdadero si la cadena de caracteres
    es encontrada dentro de la lista, falso en caso contrario.
"""

def comparar_lista_cadena(cadena, lista):
    for i, x in enumerate(lista):
        if x.find(cadena) != -1:
            return True
    return False


def barra(n=40, letra="*"):
    print(letra * n)


barra()
comparacion = comparar_lista_cadena("t", ['h', 'o', 'lo', 'a', 'd', 'e', 's', 'd', 'e', 'p', 'y', 't', 'h', 'o', 'n'])
print(comparacion)
barra()
