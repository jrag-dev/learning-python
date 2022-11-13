"""
    Se desea obtener la nómina semanal - salario neto - de los empleados de una empresa
    cuyo trabajo se paga por horas y del modo siguiente:

        1. Las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa
        determinada que debe introducir por teclado al igual que el número de horas
        y el nombre del trabajador.

        2. Las horas superiores a 35 se pagarán como extras a un promedio de 1.5 horas
        normales.

        3. Los impuestos a deducir a los trabajadores varían en función de su sueldo
        mensual:
            -- sueldo <= 2000$ , libre de impuestos
            -- los siguientes 220$ al 20%
            -- el resto, al 30%
"""

sheet = """
    ****************************************************************
    |   Programa que maneja el cálculo de nómina de un empresa.    |
    ****************************************************************
"""

print(sheet)

salario_neto = 0.0
salario_bruto = 0.0
impuestos = 0.0


nombre_empleado = str(input("\tIngrese el nombre del empleado: "))
horas_trabajadas = int(input("\tIngrese las horas trabajadas: "))
tarifa_horaria = float(input("\tIngrese la tarifa horaria: "))

# Cálculo del salario
if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_horaria
else:
    horas_extras = (horas_trabajadas - 35)
    salario_bruto = 35 * tarifa_horaria + horas_extras * tarifa_horaria * 1.5

# Cálculo de los impuestos
if salario_bruto <= 2000:
    impuestos = 0.0
elif salario_bruto <= 2220:
    impuestos = (salario_bruto - 2000)*0.20
elif salario_bruto > 2200:
    impuestos = (salario_bruto - 2220)*0.30 + (220*0.20)
else:
    print("Por favor, verificar los datos.")

# Cálculo del salario neto
salario_neto = salario_bruto - impuestos

# mostrar resultados
sheet = """
    ****************************************************************
    |      A continuación se muestran la nómina del empleado       |
    ****************************************************************
    
    Nombre del empleado: {0!s}
    Tarifa horaria: {1!s}
    Horas trabajadas: {2!s}
    
    Salario bruto: {3!s}
    Impuestos: {4!s}
    Salario Neto: {5!s}
""".format(nombre_empleado, tarifa_horaria, horas_trabajadas, salario_bruto, impuestos, salario_neto)

print(sheet)