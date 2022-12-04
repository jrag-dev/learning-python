
salario = float(input("Digite el salario para cálculo del impuesto: "))

base = salario
impuesto = 0

if base > 3000:
    impuesto = impuesto + ((base - 3000)*0.35)
    base = 3000

if base > 1000:
    impuesto = impuesto + ((base - 1000)*0.20)

print("Salario: $%6.2f Impuesto a pagar: $%6.2f" % (salario, impuesto))