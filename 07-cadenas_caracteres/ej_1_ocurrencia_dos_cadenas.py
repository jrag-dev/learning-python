"""
    Escriba un programa que lea dos cadenas de caracteres. Verifique si la segunda
    ocurre dentro de la primera e imprima la posición de comienzo.

    1ra cadena de caracteres => AABBEFAATT
    2da cadena de caracteres => BE

    Resultado => BE encontrado en la posición 3 de AABBEFAATT
"""

primera_cadena = input("Ingrese la primera cadena de texto: ")
segunda_cadena = input("Ingrese la segunda cadena de texto: ")

i = 0
while i > -1:
    i = primera_cadena.find(segunda_cadena, i)
    if i >= 0:
        print("{} encontrado en la posición {} de {}".format(segunda_cadena, i, primera_cadena))
        i += 1