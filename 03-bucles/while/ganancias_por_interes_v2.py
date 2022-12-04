"""
    Escriba un programa que pregunte el depósito inicial y la tasa de intereses de un ahorro.
    Exhiba los valores mes por mes para los primeros 24 meses.
    Escriba el lucro total por intereses en el período.
"""

deposito_inicial = float(input("Ingrese el depósito inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés: "))

mes = 1
lucro_total = 0
deposito_total = deposito_inicial

while mes <= 24:
    if mes == 1:
        deposito_mes = 0
    else:
        deposito_mes = float(input("Ingrese el depósito del %d mes: " % mes))
    deposito_total += deposito_mes

    interes = (deposito_total*tasa_interes)/100
    lucro_total += interes
    deposito_total += interes
    print("Intereses del %d mes: %10.2f $" % (mes, interes))
    mes += 1

print("El lucro total por intereses es: %10.2f$" % lucro_total)
