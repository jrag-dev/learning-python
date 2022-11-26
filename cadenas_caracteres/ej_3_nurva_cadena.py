"""
    Escriba un programa que lea dos cadenas de texto y genere una tercera con los caracteres
    que aparacen en una de ellas.

    1ra cadena de texto => CTA
    2da cadena de texto => ABC
    3ra cadena de texto => BT

    el orden de los caracteres de la tercera cadena de texto no es importante.
"""

primera_cadena = input("Ingrese la primera cadena de texto: ")
segunda_cadena = input("Ingrese la segunda cadena de texto: ")
tercera_cadena = ""

i = 0
while i < len(primera_cadena):
    if segunda_cadena.find(primera_cadena[i]) == -1:
        tercera_cadena = tercera_cadena + primera_cadena[i]
    i += 1

j = 0
while j < len(segunda_cadena):
    if primera_cadena.find(segunda_cadena[j]) == -1:
        tercera_cadena = tercera_cadena + segunda_cadena[j]
    j += 1

print("Tercera cadena: %s" % tercera_cadena)