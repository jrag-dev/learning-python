"""
    Escriba un programa que lea dos números y que pregunte que operación desea
    realizar. Usted debe poder cálcular la suma (+), sustracción (-), multiplicación (*)
    y división (/). Muestre el resultado de la operación.
"""

def menu():
    opciones = """
        ¿Qué tipo de cálculo desea realizar?
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        0. Salir
    """
    print(opciones)


menu()
operacion = int(input("Operación a realizar: "))
while 0 >= operacion > 4:
    operacion = int(input("Operación a realizar: "))

num1 = float(input("\nIngrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

mensaje = None

if operacion == 1:
    suma = num1 + num2
    mensaje = """
        Número 1: {0!s}
        Número 2: {1!s}
        Suma: {2!s}
    """.format(num1, num2, suma)
elif operacion == 2:
    resta = num1 - num2
    mensaje = """
        Número 1: {0!s}
        Número 2: {1!s}
        Resta: {2!s}
    """.format(num1, num2, resta)
elif operacion == 3:
    multiplicacion = num1*num2
    mensaje = """
        Número 1: {0!s}
        Número 2: {1!s}
        Multiplicación: {2!s}
    """.format(num1, num2, multiplicacion)
elif operacion == 4:
    division = (num1/num2)
    mensaje = """
        Número 1: {0!s}
        Número 2: {1!s}
        División: {2!s}
    """.format(num1, num2, division)
else:
    mensaje = "Operacion no soportada!"

print(mensaje)