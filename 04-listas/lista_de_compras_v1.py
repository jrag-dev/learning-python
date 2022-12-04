"""
    Programa que lee e imprime una lista de compras hasta que sea digitado fin.
"""

compras = []

while True:
    producto = input("Producto: ")

    if producto == "fin":
        break

    compras.append(producto)

for p in compras:
    print(p)