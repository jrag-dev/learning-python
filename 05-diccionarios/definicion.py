"""
    Los diccionarios consisten en una estructura de datos similar a las listas, pero
    con propiedades de acceso diferentes. Está compuesto por un conjunto de claves
    y valores.
"""

tabla = {
    "Lechuga": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Poroto": 1.50
}

print(tabla)

print(tabla["Lechuga"])
tabla["Pera"] = 0.98
tabla["Lechuga"] = 0.36

print(tabla)

if "Tomate" in tabla:
    print("Encontrado")


# Obtención de una lista de claves y valores
print(tabla.keys())
print(tabla.values())