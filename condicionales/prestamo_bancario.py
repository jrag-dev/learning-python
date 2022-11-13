"""
    Escriba un programa para aprobar el préstamo bancario para la compra de
    una casa. El programa debe preguntar el valor de la casa a comprar, el
    salario y la cantidad de años a pagar. El valor de la cuota mensual no
    puede ser superior a 30% del salario. Calcule el valor de la cuota
    dividiendo el valor de la casa a comprar por él número de meses a pagar.
"""

valor_casa = float(input("¿Precio de la casa a comprar: "))
salario = float(input("Salario del comprador: "))
cantidad_years = int(input("Cantidad de años para pagar la casa: "))

valor_cuota = valor_casa/cantidad_years

limite = salario*0.30

if valor_cuota > limite:
    print("El valor de la cuota no puede ser mayor al 30% del salario")
else:
    mensaje = """
        Valor de la cuota de la casa:
        Salario del comprador: {0!s} $
        Valor de la casa: {1!s} 4
        Número total de cuotas: {2!s} cuotas
        Valor de la cuota: {3!s} $
    """.format(salario, valor_casa, cantidad_years, valor_cuota)
    print(mensaje)