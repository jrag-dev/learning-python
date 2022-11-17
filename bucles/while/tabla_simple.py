"""
    Escribir un programa que imprima la tabla de sumar de un número digitado por
    el usuario
"""

n = int(input("Tabla de: "))

x = 1
while x <= 10:
    print(n + x)
    x = x + 1