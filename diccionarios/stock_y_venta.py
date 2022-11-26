stock = {
    "tomate": [1000, 2.30],
    "lechuga": [500, 0.50],
    "batata": [2001, 1.20],
    "poroto": [100, 1.50]
}

venta = [["tomate", 5], ["batata", 10], ["lechuga", 5]]
total = 0

print("Ventas:\n")
for operacion in venta:
    producto, cantidad = operacion
    precio = stock[producto][-1]
    costo = precio*cantidad
    print("%12s: %3d x %6.2f = %6.2f" % (producto, cantidad, precio, costo))
    stock[producto][0] -= cantidad
    total += costo

print("\t Costo total: %18.2f\n" % total)
print("Stock:\n")
for clave, valor in stock.items():
    print("Descripción: ", clave)
    print("Cantidad: ", valor[0])
    print("Precio: %6.2f\n" % valor[-1])