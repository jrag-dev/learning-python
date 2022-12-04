
precio: float = 0

categoria: int = int(input("Digite la categoria del producto: "))

while categoria <= 0:
    print("La categoria debe ser un entero mayor a cero!")
    categoria = int(input("Digite la categoria del producto: "))

if categoria == 1:
    precio = 10
elif categoria == 2:
    precio = 18
elif categoria == 3:
    precio = 23
elif categoria == 4:
    precio = 26
elif categoria == 5:
    precio = 31
else:
    print("¡Categoría inválida, digite un valor entre 1 y 5!")

resultado = """
    Categoria: {0!s}
    Precio del producto: {1!s} $
""".format(categoria, precio)

print(resultado)