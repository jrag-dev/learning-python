"""
    Escribir un programa que lea un valor y que imprima la cantidad de billetes
    necesarios para pagar ese mismo valor. Trabajar con valores enteros y con
    billetes de 50, 20, 10, 5 y 1 $.
"""

valor = int(input("Digite el valor a pagar: "))

while valor <= 0:
    valor = int(input("Digite el valor a pagar: "))

billetes = 0
actual = 100
apagar = valor

while True:
    if actual <= apagar:
        apagar -= actual
        billetes += 1
    else:
        print("%d billete(s) de $%d" % (billetes, actual))

        if apagar == 0:
            break
        if actual == 100:
            actual = 50
        elif actual == 50:
            actual = 20
        elif actual == 20:
            actual = 10
        elif actual == 10:
            actual = 5
        elif actual == 5:
            actual = 1

        billetes = 0