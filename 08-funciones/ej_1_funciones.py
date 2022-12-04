"""
    Escriba una función que retorne el mayor de dos números.

    se espera: maximo(5,6) == 6
"""

def maximo(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a


maximo56 = maximo(5, 6)
maximo73 = maximo(7, 3)
maximo99 = maximo(9, 9)

print("Máximo(5, 6) = {0:<10} \nMáximo(7, 3) = {1:<10} \nMáximo(9, 9) = {2:<10}".format(maximo56, maximo73, maximo99))