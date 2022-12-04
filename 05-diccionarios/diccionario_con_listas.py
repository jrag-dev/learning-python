"""
    Relación de stock de mercaderías donde tendremos además del precio, la
    cantidad de mercadería en stock.
"""

stock = {
    "tomate": [1000, 2.30],
    "lechuga": [500, 0.50],
    "batata": [2001, 1.20],
    "poroto": [100, 1.50]
}

print("\tProducto \tCantidad \tPrecio")
for claves, valor in stock.items():
    producto = claves
    cantidad = valor[0]
    precio = valor[-1]
    print("\t%7s \t%6s \t%9s" % (producto, cantidad, precio))