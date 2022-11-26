"""
    Las tuplas es una estructura de datos que se caracteriza por ser inmutables. Es decir,
    una vez que se define la tupla, no se pueden modificar sus elementos.
"""

# definir una tupla

tupla = (1, 2, 'tres', 'cuatro')
var1 = tupla[2]
var2 = tupla[1:3]

print("Tupla[2]: ", var1)
print("Tupla[1:3]: ", var2)

# recorrer tuplas

for elemento in tupla:
    print("Elementos: ", elemento)

# obtener su longitud

largo = len(tupla)
print("Longitud de la tupla: ", largo)

# Saber si un elemento esta en una tupla

var3 = 'cuatro' in tupla
print(var3)

# Unir dos tuplas con el operador +

tupla1 = (1, 2, 'tres', 'cuatro')
tupla2 = (5, 6, "siete")
tupla = tupla1 + tupla2
print(tupla)

# se puede crear una tupla con un solo item pero debe terminar con una coma (,)

mi_tupla = (1,)
print(mi_tupla)
print(type(mi_tupla))

# Se puede transformar a tupla una lista

lista = [1, 2, 3, 4, 5]
tupla_lista = tuple(lista)
print(tupla_lista)
print(type(tupla_lista))

# Se puede transformar una tupla a lista

tupla = (1, 2, 3, 4, 5)
lista_tupla = list(tupla)
print(lista_tupla)
print(type(lista_tupla))