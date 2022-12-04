"""
    Escriba un programa que lea dos cadenas de caracteres y genere una tercera,
    en la cual los caracteres de la segunda hayan sido retirados de la primera.

    1ra cadena de caracteres => AATTGGAA
    2da cadena de caracteres => TG
    3ra cadena de caracteres => AAAA
"""

primera_cadena = input("Ingrese la primera cadena de texto: ")
segunda_cadena = input("Ingrese la segunda cadena de texto: ")
tercera_cadena = ""

indices = []
i = 0
while i < len(primera_cadena):
    for j in segunda_cadena:
        if primera_cadena[i] == j:
            indices.append(i)
    i += 1

j = 0
while j < len(primera_cadena):
    if j not in indices:
        tercera_cadena = tercera_cadena + primera_cadena[j]
    j += 1


print(tercera_cadena)
