"""
    Generar un número aleatorio entre 1 y 10. Preguntar al usuario que adivine el número
    e imprima un mensaje indicando si el número ingresado es menor o mayor que el
    número generado.
"""
from random import random
from math import floor

head = """
    Programa que genera un número aleatorio y permite 5 intentos al usuario
    para que lo pueda adivinar!!
"""
print(head)


def generar_random():
    num = floor(random() * 10 + 1)
    return num


aleatorio = generar_random()
intentos = 0
adivinado = False


while intentos < 5 or adivinado:
    numero = int(input("\tIngrese un número entre 01 y 10: "))
    if numero > aleatorio:
        print("\tEl número ingresado es mayor")
        intentos += 1
    elif numero < aleatorio:
        print("\tEl número ingresado es menor")
        intentos += 1
    else:
        intentos += 1
        sheet = """
            Felicidades!!
            Lograste adivinar el número aleatorio en {0!s} intentos
        """.format(intentos)
        print(sheet)
