"""
    Teoría de como usar los diccionarios en python
"""

mi_dicc = dict()  # Crea un diccionario vacío

mi_diccionario = {}  # Otra forma de crear un diccionario en python

diccionario = {
    1: 'palabra1',
    2: 'palabra2'
}

""" ************* Busqueda sobre un diccionario ************* """

valor = diccionario[2]
print(valor)

""" ************* insertar sobre un diccionario ************* """

diccionario[3] = "palabra3"

print(diccionario)

""" ************* Eliminar sobre un diccionario ************* """

del diccionario[1]

print(diccionario)

# lista con todas las llaves del diccionario

lista_keys = list(diccionario.keys())
print(lista_keys)

# Lista con todos los valores del diccionario

lista_values = list(diccionario.values())
print(lista_values)

# Lista con todos los indices del diccionario

lista_items = list(diccionario.items())
print(lista_items)

# Saber si una clave forma parte del diccionario

clave = 4 in diccionario
print(clave)

llave = 2 in diccionario
print(llave)
