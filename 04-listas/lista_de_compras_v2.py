compras = []

while True:
    producto = input("Producto: ")

    if producto == "fin":
        break

    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))

    compras.append([producto, cantidad, precio])

total = 0.0
for e in compras:
    print("%20s x%5d %5.2f %6.2f" % (e[0], e[1], e[2], e[1]*e[2]))

    total += e[1]*e[2]

print("Total de compra: %7.2f" % total)