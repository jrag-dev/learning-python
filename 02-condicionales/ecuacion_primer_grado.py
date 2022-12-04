"""
    Escriba un programa para encontrar las soluciones de la ecuación de primer
    grado
                a*x + b = 0
    donde a y b son los datos.
"""

head = """
    **********************************************************
    |   Programa que resuelve la ecuación de primer grado.   |
    |                                                        |
    |   a*x + b = 0. Debes ingresar los valores de a y b     |
    **********************************************************
"""
print(head)

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

if a > 0:
    x = -b/a
    print("solución: %10.2f" % x)
else:
    if b == 0:
        print("Solución imposible!!")
    else:
        print("Solución indeterminada")