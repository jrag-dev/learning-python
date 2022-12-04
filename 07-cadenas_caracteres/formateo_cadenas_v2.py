"""
    Limitación del tamaño de impresión de los parámetros
"""

formato1 = "{0:10} {1}".format("123", "456")
print(formato1)

formato2 = "X{0:10}X".format("123456789012345")
print(formato2)

formato3 = "X{0:10}X".format("123")
print(formato3)

# Especificación de espacios a la izquierda o a la derecha

formato4 = "X{0:<10}X".format("123")
print(formato4)

formato5 = "X{0:>10}X".format("123")
print(formato5)

# Si queremos centrar el valor entre los espacios, podemos usar el acento circunflejo (^)

formato6 = "X{0:^10}X".format("123")
print(formato6)