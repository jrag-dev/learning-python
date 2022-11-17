"""
    Escriba un programa que lea números enteros del teclado. El programa debe leer los
    números hasta que el usuario digite -1. al final de la ejecución, exhiba la cantidad
    de números digitados, así como la suma y la media aritmética.
"""

suma = 0
contador = 0

while True:
    numero = float(input("Digite un número entero o -1 para salir: "))

    if numero == -1:
        break

    contador += 1
    suma += numero

print("Números digitados: %d" % contador)
print("La sumatoria es: %10.2f" % suma)