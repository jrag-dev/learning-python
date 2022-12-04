"""
    Escriba un programa que lea una cadena de caracteres e imprima cuántas veces cada
    carácter aparece en esa cadena de caracteres.

    cadena de caracteres => TTAAC
    Resultado:
    T: 2x
    A: 2x
    C:1x
"""

cadena = "TTAACPRTTACAA"

i = 0
dicc = {}
while i < len(cadena):
    if cadena[i] in dicc:
        dicc[cadena[i]] += 1
    else:
        dicc[cadena[i]] = 1
    i += 1

print("Resultado:")
for clave, valor in dicc.items():
    print("{}: {}x".format(clave, valor))