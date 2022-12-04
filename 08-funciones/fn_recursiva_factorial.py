"""
    Función recursiva que usamos para calcular el factorial de un número entero
"""

def factorial(n):
    print("Calculando el factorial de %d" % n)
    if n == 0 or n == 1:
        print("Factorial de %d = 1" % n)
        return 1
    else:
        fact = n*factorial(n-1)
        print("factorial de %d = %d" %(n, fact))
        return fact


print(factorial(12))