"""
    Escriba un programa para controlar una pequeña máquina registradora. Usted debe solicitarle
    al usuario que digite el código del producto y la cantidad comprada. Utilice la tabla
    de códigos que aparece abajo para obtener el precio de cada producto.

    El programa debe exhibir el total de las compras
"""
def menu():
    opciones = """
    A continuación se muestran los códigos 
    y precios de cada producto:
    
        código  |   Precio
           1    |    0.50
           2    |    1.00
           3    |    4.00
           5    |    7.00
           9    |    8.00
    """
    print(opciones)


total_compras = 0.0
n_productos = 0

while True:
    menu()

    codigo = int(input("Ingrese el código del producto: "))
    precio = 0.00

    if codigo == 0:
        break

    if codigo == 1:
        precio = 0.50
    elif codigo == 2:
        precio = 1.00
    elif codigo == 3:
        precio = 4.00
    elif codigo == 5:
        precio = 7.00
    elif codigo == 9:
        precio = 8.00
    else:
        print("Código inválido!!")

    total_compras = total_compras + precio
    n_productos += 1


sheet = """
    Total de productos comprados: {0!s}
    Total de compras: {1:10.2f} $
""".format(n_productos, total_compras)
print(sheet)