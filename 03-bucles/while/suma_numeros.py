"""
    Escribir un programa para calcular el total de una suma.
"""

n = 1
suma = 0

while n <= 10:
    x = int(input("Digite el %d número: " % n))
    suma = suma + x
    n = n + 1

print("Suma: %d" % suma)