"""
    Busqueda de un elemento de la lista usando el método secuencial y
    la sentencia for
"""

L = [7, 9, 10, 12, 5]

elemento = int(input("Ingrese un número a buscar: "))

for item in L:
    if item == elemento:
        print("¡Elemento encontrado!")
        break
else:
    print("Elemento no encontrado!")