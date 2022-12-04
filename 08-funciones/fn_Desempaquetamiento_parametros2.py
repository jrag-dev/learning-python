"""
    Función con número indeterminado de parámetros
"""

def imprime_mayor(mensaje, *numeros):
    mayor = None
    for x in numeros:
        if mayor is None or mayor < x:
            mayor = x

    print(mayor)


imprime_mayor("Mayor", 5, 4, 3, 2, 1)
imprime_mayor("Max: ", *[1, 7, 9, 5])