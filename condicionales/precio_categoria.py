
categoria = int(input("Digite la categoria del producto: "))
precio: float = 0

while categoria < 0:
    print("La categoria debe ser un entero mayor a cero!")
    categoria = int(input("Digite la categoria del producto: "))

if categoria == 1:
    precio = 10
else:
    if categoria == 2:
        precio = 18
    else:
        if categoria == 3:
            precio = 23
        else:
            if categoria == 4:
                precio = 26
            else:
                if categoria == 5:
                    precio = 31
                else:
                    print("¡Categoría inválida, digite un valor entre 1 y 5!")

resultado = """
    Datos del producto:
    Categoria: {0!s}
    Precio: {1!s} $
""".format(categoria, precio)

print(resultado)