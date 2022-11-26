stock = {
    "tomate": [1000, 2.30],
    "lechuga": [500, 0.50],
    "batata": [2001, 1.20],
    "poroto": [100, 1.50]
}

venta = []
while True:
    head = """
        Carrito de compras:
        Agregar producto => "agregar"
        Realizar compra  => "comprar"
    """
    opcion = input("Ingrese su opción: ")

    if opcion == "comprar":
        break
    elif opcion == "agregar":
        producto = input("Ingrese el producto a comprar: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        venta.append([producto, cantidad])
    else:
        print("Operación no permitida!!")


total = 0.0

print("Ventas: \n")
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
    producto = clave
    cantidad = valor[0]
    precio = valor[-1]
    print("Descripción: %s" % producto)
    print("Cantidad: %s" % cantidad)
    print("Precio: %s\n" % precio)