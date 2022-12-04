"""
    Formas de formatear cadenas de caracteres en python
"""

saludo = "{0} {1}".format("Hola", "Mundo")
print(saludo.center(20, "*"))

factura = "{0} x {1} ${2}".format(5, "Manzana", "1.20")
print(factura)

formato1 = "{0} {1} {0}".format("_", "_")
formato2 = "{0} {1} {0}".format("_", "_")
formato3 = "{0} {1} {0}".format("_", "_")
print(formato1)
print(formato2)
print(formato3)

formato1 = "{0} {1} {0}".format("_", "O")
formato2 = "{0} {1} {0}".format("_", "_")
formato3 = "{0} {1} {0}".format("_", "_")
print(formato1)
print(formato2)
print(formato3)

formato1 = "{0} {1} {0}".format("_", "O")
formato2 = "{0} {1} {0}".format("_", "X")
formato3 = "{0} {1} {0}".format("_", "_")
print(formato1)
print(formato2)
print(formato3)

formato1 = "{0} {1} {0}".format("_", "O")
formato2 = "{0} {1} {0}".format("_", "X")
formato3 = "{0} {1} {0}".format("_", "O")
print(formato1)
print(formato2)
print(formato3)