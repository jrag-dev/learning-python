from math import floor

head = """
    *************************************************************
    |   Programa que permite desglosar una cantidad de dinero   |
    |   Suministrada en los diferentes billetes y monedas en $  |
    *************************************************************
"""
print(head)

cantidad_dinero = int(input("\tIngrese la cantidad de dinero: $"))

cantidad = cantidad_dinero

resto = cantidad % 500
billetes_500 = floor(cantidad / 500)

cantidad = resto
billetes_200 = floor(cantidad/200)
resto = cantidad % 200

cantidad = resto
billetes_100 = floor(cantidad/100)
resto = cantidad % 100

cantidad = resto
billetes_50 = floor(cantidad/50)
resto = cantidad % 50

cantidad = resto
billetes_20 = floor(cantidad/20)
resto = cantidad % 20

cantidad = resto
billetes_10 = floor(cantidad/10)
resto = cantidad % 10

cantidad = resto
billetes_5 = floor(cantidad/5)
resto = cantidad % 5

cantidad = resto
monedas_2 = floor(cantidad/2)
resto = cantidad % 2

cantidad = resto
monedas_1 = floor(cantidad/1)
resto = cantidad % 1

sheet = """
    Cantidad de dinero: {0!s}$
    Se puede desglosar de la siguiente manera: 
""".format(cantidad_dinero)
print(sheet)

if billetes_500 > 0:
    print("\t%s billetes de 500$" % billetes_500)
if billetes_200 > 0:
    print("\t%s billetes de 200$" % billetes_200)
if billetes_100 > 0:
    print("\t%s billetes de 100$" % billetes_100)
if billetes_50 > 0:
    print("\t%s billetes de 50$" % billetes_50)
if billetes_20 > 0:
    print("\t%s billetes de 20$" % billetes_20)
if billetes_10 > 0:
    print("\t%s billetes de 10$" % billetes_10)
if billetes_5 > 0:
    print("\t%s billetes de 5$" % billetes_5)
if monedas_2 > 0:
    print("\t%s monedas de 2$" % monedas_2)
if monedas_1 > 0:
    print("\t%s monedas de 1$" % monedas_1)