"""
    Escribir un programa que imprima solo los números pares entre 0 y un valor definido
    por el usuario
"""

fin = int(input("Digite el último número a imprimir: "))

x = 0
while x <= fin:
    if x % 2 == 0:
        print(x)
    x += 1