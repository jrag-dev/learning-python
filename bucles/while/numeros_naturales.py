"""
    Mostrar los N primeros números naturales en forma descendiente
"""

N = int(input("Entra un número natural: "))


i = N
while i >= 1:
    print(i, end=" ")
    i = i - 1