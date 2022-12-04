"""
    Escriba un programa que muestre un menu de opciones que pidan al usuario
    si quiere calcular el diámetro, perímetro o área
"""

from math import pi

radio = float(input("Dame el radio de un círculo: "))

# Menu
print("Escoge una opción: ")
print("a) Calcular el diámetro.")
print("b) Calcular el perímetro.")
print("c) Calcular el área.")

opcion = (input("Teclea una de las opciones: ")).lower()

if opcion == "a":
    diametro = 2*radio
    print("El diámetro es: {0:10.2f}".format(diametro))
else:
    if opcion == "b":
        perimetro = 2*pi*radio
        print("El perímetro es: {0:10.2f}".format(perimetro))
    else:
        if opcion == "c":
            area = pi*radio**2
            print("El área del círculo es: {0:10.2f}".format(area))
        else:
            print("Sólo hay tres opciones: a, b, c.")
            print("Tú has tecleado: '{0}'".format(opcion))