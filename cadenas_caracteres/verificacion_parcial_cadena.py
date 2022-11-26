"""
    Cuando se necesita saber si una cadena de caracteres comienza o termina
    con algunos caracteres
"""

nombre = "Juan da Silva"
is_content = nombre.startswith("J")
print(is_content)

is_content = nombre.startswith("j")
print(is_content)

is_finally = nombre.endswith("Silva")
print(is_finally)
