"""
    Especificación de espacios a la izquierda o a la derecha
"""

formato1 = "X{0:.<10}X".format("123")
print(formato1)

formato2 = "X{0:!>10}X".format("123")
print(formato2)

formato3 = "X{0:*^10}X".format("123")
print(formato3)