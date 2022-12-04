"""
    Se puede crear funciones que reciben un número indeterminado de parámetros
    utilizando listas de parámetros.
"""

def suma(*args):
    s = 0
    for x in args:
        s += x
    return s


print(suma(1, 2))
print(suma(2))
print(suma(5, 6, 7, 8))
print(suma(9, 10, 20, 30, 40))