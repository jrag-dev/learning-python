"""
    Escribir un programa que reciba un año y muestre si es ó será un año
    bisiesto.
"""

head = """
    **************************************************************
    |   Programa que determina si un año pasado por el usuario   |
    |   es bisiesto o no.                                        |
    **************************************************************
"""
print(head)

year = int(input("Ingrese un año: "))

bisiesto = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            bisiesto = True
        else:
            bisiesto = False
    else:
        bisiesto = True
else:
    bisiesto = False

sheet = """
    Año ingresado: {0!s} {1!s}
""".format(year, ("es/será un año bisiesto" if bisiesto is True else "no es/será un año bisiesto"))
print(sheet)