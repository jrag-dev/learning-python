"""
    Escriba un programa que pregunte el salario del empleado y calcule el valor
    del aumento. Para salarios superiores a 1250, calcule un aumento de 10%. Para
    infeiores o iguales, de 15%.
"""

salario = float(input("Ingrese el salario del empleado: "))

base = salario
aumento = 0

if base > 1250:
    aumento = aumento + (base*0.10)
    base = 1250
if base <= 1250:
    aumento = aumento + (base*0.15)

total = salario + aumento

resultado = """
    Salario base: {0!s}
    Aumento: {1!s}
    Salario Ajustado: {2!s}
""".format(salario, aumento, total)

print(resultado)