"""
    Convertir una cadena de texto en lista para poder modificarla
"""

L = list("Hola mundo")

L[0] = "a"

print(L)

s = "".join(L)
print(s)