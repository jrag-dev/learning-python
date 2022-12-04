"""
    Escribir un programa que pregunte la velocidad del auto de un usuario.
    En caso de que supere los 80 km/h, exhiba un mensaje diciendo que el
    usuario fue multado. En este caso, exhiba el valor de la multa, cobrando
    5$ por cada km encima de 80km
"""

limite = 80
multa = False
total = 0

velocidad = float(input("¿Cuál es la velocidad del auto? "))

if velocidad > limite:
    multa = True
    print('El usuario a sido multado!')

if multa:
    total = (velocidad - limite)*5


resultado = """
    Limite de Velocidad: {0!s} km/h
    Velocidad: {1!s} km/h
    Multa a Pagar: {2!s} $
""".format(limite, velocidad, total)

print(resultado)