"""
    Escribir un programa que determine cual es el mayor de tres números pasados por
    el usuario
"""

head = """
    *****************************************************
    |   Programa que cálcula el mayor de tres números   |
    |                                                   |
    *****************************************************
"""

print(head)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 > num2:
    if num1 > num3:
        maximo = num1
    else:
        maximo = num3
else:
    if num2 > num3:
        maximo = num2
    else:
        maximo = num3

sheet = """
    El máximo es: {0:10.2f}
""".format(maximo)
print(sheet)