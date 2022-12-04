"""
    Escriba un programa que lea tres números y que imprima el mayor y el menor
"""

x = float(input("Ingrese el primer número, x = "))
y = float(input("Ingrese el segundo número, y = "))
z = float(input("Ingrese el tercer número, z = "))

mayor = 0
medio = 0
menor = 0


if x > y > z:
    mayor = x
    medio = y
    menor = z
elif x > z > y:
    mayor = x
    medio = z
    menor = y
elif y > x > z:
    mayor = y
    medio = x
    menor = z
elif y > z > x:
    mayor = y
    medio = z
    menor = x
elif z > x > y:
    mayor = z
    medio = x
    menor = y
elif z > y > x:
    mayor = z
    medio = y
    menor = x
elif x == y and y > z:
    mayor = x
    medio = y
    menor = z
elif x == y and z > y:
    mayor = z
    medio = y
    menor = x
elif z == x and x > y:
    mayor = z
    medio = x
    menor = y
elif z == x and y > x:
    mayor = y
    medio = z
    menor = x
elif z == y and y > x:
    mayor = z
    medio = y
    menor = x
elif z == y and x > y:
    mayor = x
    medio = z
    menor = y
else:
    print("Números incorrectos")


resultados = """
    Mayor: {0!s}
    Menor: {1!s}
""".format(mayor, menor)

print(resultados)