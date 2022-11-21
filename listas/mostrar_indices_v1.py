"""
    Mostrar indices sin usar la función enumerate
"""

L = [4, 6, 7, 9, 12]

x = 0
for item in L:
    print("[%d] %d" % (x, item))
    x += 1