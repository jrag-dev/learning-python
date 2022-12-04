"""
    Función que permite obtener el factorial de un número entero.
"""

def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact


print(factorial(8))