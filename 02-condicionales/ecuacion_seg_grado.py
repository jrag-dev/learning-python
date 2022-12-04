"""
    Escriba un programa para encontrar las soluciones de una ecuación de
    segundo grado
"""

from math import sqrt

head = """
    ==========================================================================
    |    Programa que cálcula las raices de una ecuación de segundo grado   |
    ==========================================================================
"""
print(head)

a = float(input("\tValor del coeficiente a: "))
b = float(input("\tValor del coeficiente b: "))
c = float(input("\tValor del coeficiente c: "))

print("")

if a == 0:
    print("\tNo tenemos una ecuación de segundo grado!!")
else:
    d = b**2 - 4*a*c
    if d == 0:
        x1 = -b/2*a
        sheet = """
            x1 = {0:.3f}
        """.format(x1)
        print(sheet)
    elif d > 0:
        x1 = (-b + sqrt(d))/2*a
        x2 = (-b - sqrt(d))/2*a
        sheet = """
            x1 = {0:.3f}
            x2 = {1:.3f}
        """.format(x1, x2)
        print(sheet)
    else:
        xr = -b/2*a
        xi = sqrt(-d)/2*a
        print(f'\tx1 = {xr} + i*{xi}')
        print(f'\tx2 = {xr} - i*{xi}')