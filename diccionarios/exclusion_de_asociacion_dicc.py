tabla = {
    "Lechuga": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Poroto": 1.50
}

head = """
    Puede realizar las siguientes operaciones:
    
    1. Añadir nuevo producto  => insert
    2. Eliminar un producto   => delete
    3. Actualizar un producto => update
    4. Mostrar todos los productos => read
"""
print(head)


def mostrar_productos():
    print("\tTenemos los siguientes productos hasta el momento: ")
    i = 1
    for clave, datos in tabla.items():
        print("\t%2s. %4s: %5s$" % (i, clave, datos))
        i += 1


def agregar_producto(producto, precio):
    tabla[producto] = precio


def delete_producto(producto):
    del tabla[producto]


def update_producto(producto, precio):
    tabla[producto] = precio


opcion = input("Escriba su opción: ")

while True:

    if opcion == "q":
        break
    elif opcion == "read":
        mostrar_productos()
    elif opcion == "insert":
        prod = input("Ingrese el nombre del producto a agregar: ")
        costo = input("Ingrese el precio del producto a agregar: ")
        agregar_producto(prod, costo)
    elif opcion == "update":
        prod = input("Ingrese el nombre del producto a agregar: ")
        costo = input("Ingrese el precio del producto a agregar: ")
        update_producto(prod, costo)
    elif opcion == "delete":
        p = input("Ingrese el nombre del producto a eliminar: ")
        delete_producto(p)
    else:
        print("Operación no soportada!")

    opcion = input("Escriba su opción: ")
