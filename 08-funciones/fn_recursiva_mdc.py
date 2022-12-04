"""
    Función recursiva que calcula el mayor divisor común (M.D.C) entre dos números
    a y b, donde a > b.
"""

def mdc(a, b):
    if b == 0:
        return a
    if a > b:
        mcd = mdc(b, (a % b))
        return mcd


print(mdc(7, 2))
print(mdc(21, 7))
print(mdc(16, 8))
print(mdc(24, 18))
print(mdc(6, 4))

