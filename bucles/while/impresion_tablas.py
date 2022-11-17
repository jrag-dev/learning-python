"""
    Realizar un programa que imprima las tablas de multiplicar del 1 al 10.
"""

tabla = 1
while tabla <= 10:
    numero = 1
    while numero <= 10:
        print("%d x %d = %d" % (tabla, numero, tabla*numero))
        numero += 1
    tabla += 1

