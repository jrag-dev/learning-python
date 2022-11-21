"""
    Programa que termite añadir elementos a una lista por teclado
    hasta ingresar el número 0
"""

L = []

while True:
    n = int(input("Ingrese un número (0 para salir): "))

    if n == 0:
        break
    L.append(n)

x = 0
while x < len(L):
    print(L[x], end=" ")
    x = x + 1