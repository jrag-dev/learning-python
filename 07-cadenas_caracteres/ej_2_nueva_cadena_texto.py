"""
    Escriba un programa que lea dos cadenas de texto y genere una tercera con
    los caracteres comunes de las dos cadenas leidas.
"""

primera_cadena = input("Ingrese la primera cadena de texto: ")
segunda_cadena = input("Ingrese la segunda cadena de texto: ")
tercera_cadena = ""

for i in primera_cadena:
    for j in segunda_cadena:
        if j == i:
            tercera_cadena = tercera_cadena + j
            # print(j, end=" ")

print(tercera_cadena)