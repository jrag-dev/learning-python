"""
    Escriba un programa que pregunte el valor inicial de una deuda y el interés mensual.
    Pregunte también el valor mensual que será pagado. Imprima el número de meses para
    que la deuda sea pagada, el total pagado y el total de intereses pagado.
"""

deuda_inicial = float(input("Ingrese el valor de la deuda inicial: "))
interes_mensual = float(input("Ingrese el interés mensual: "))
cuota_mensual = float(input("Ingrese la cuota mensual a pagar: "))

deuda = deuda_inicial
mes = 1
interes = 0
ganacias_interes = 0

while deuda > 0:

    interes = (deuda * interes_mensual) / 100
    deuda = deuda + interes - cuota_mensual

    print("Mes: %s" % mes)
    print("interes: %10.2f" % interes)
    print("Deuda: %10.2f" % deuda)

    mes += 1
