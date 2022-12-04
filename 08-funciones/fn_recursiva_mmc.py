"""
    Función que permite calcular el menor múltiplo común (M.M.C) entre dos números.
"""

def mdc(a, b):
    if b == 0:
        return a
    if a > b:
        mcd = mdc(b, (a % b))
        return mcd


def mmc(a, b):
    if a > b:
        mcm = (abs(a*b)/mdc(a, b))
        return mcm
    else:
        print("a debe ser mayor que b")


print(mmc(6, 4))