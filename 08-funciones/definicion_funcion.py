"""
    Definiendo nuestras propias funciones
"""


def suma(a, b):
    print(a + b)


suma(2, 9)
suma(7, 8)
suma(10, 15)


def sumatoria(a, b):
    return a + b


suma = sumatoria(5, 7)
print(suma)

def espar(x):
    return x % 2 == 0


print(espar(2))
print(espar(3))
print(espar(10))