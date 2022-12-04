"""
    Ejemplo de como mostrar una lista lista usando el bucle for
"""

L = [4, 8, 9, 11, 2]

for item in L:
    print(item)

print("")

i = 0
while i < len(L):
    for item in L:
        print("µ", end=" ")

    print("\r")
    i += 1

print("")

j = 0
while j < len(L):
    item = L[j]
    print(item)
    j += 1