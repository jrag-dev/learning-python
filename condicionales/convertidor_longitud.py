"""
    Escribir un programa que pregunte al usuario una long en centimetros. Sí
    el usuario introduce una long negativo, el programa debe indicar al usuario
    que el valor ingresado es invílido. De otra forma, el programa debe convertir
    la long a inches e imprimir el resultado. 1 inch => 2.54 cm
"""

head = """
    ************************************************************
    |    Programa que realiza la conversión de una longitud     |
    |    ingresada en centimetros a inches.                     |
    ************************************************************
"""
print(head)

long_inches = 0.0
longitud = float(input("Ingrese la long en centimetros: "))


def convertir(long):
    return long / 2.54


if longitud < 0:
    print("Longitud inválida.")
else:
    long_inches = convertir(longitud)
    sheet = """
        Longitud en cm: {0:10.2f}
        Longitud en inch: {1:10.2f}
    """.format(longitud, long_inches)
    print(sheet)