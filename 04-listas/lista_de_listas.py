producto1 = ["manzana", 10, 0.30]
producto2 = ["pera", 5, 0.75]
producto3 = ["kiwi", 3, 0.98]

compras = [producto1, producto2, producto3]

print("Compras: ", compras)

for item in compras:
    producto = item[0]
    cantidad = item[1]
    precio = item[2]
    sheet = """
            Producto: {0!s}
            Cantidad: {1!s}
            Precio: {2!s}
        """.format(producto, cantidad, precio)
    print(sheet)
