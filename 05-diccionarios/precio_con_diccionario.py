tabla = {
    "Lechuga": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Poroto": 1.50
}

while True:
    producto = input("Ingrese el nombre del producto, fin para terminar: ")

    if producto == "fin":
        break

    if producto in tabla:
        print("Precio %5.2f" % tabla[producto])
    else:
        print("¡Producto no encontrado!")