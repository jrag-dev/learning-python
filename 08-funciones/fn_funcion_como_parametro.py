"""
    Ejemplo de como se pueden pasar funciones como parámetros en otras funciones
"""

def suma(a, b):
    return a + b

def sustraccion(a, b):
    return a - b

def imprime(a, b, foper):
    print(foper(a, b))


imprime(5, 4, suma)
imprime(9, 7, sustraccion)