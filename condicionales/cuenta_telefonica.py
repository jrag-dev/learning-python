"""
    Calcular la cuenta de un teléfono celular de la empresa Movistar. Los planes
    de la empresa Movistar son muy interesantes y ofrecen precios diferenciados
    de acuerdo con la cantidad de minutos usados por mes. Abajo de 200 minutos
    la empresa cobra 0.20$ por minutos. Entre 200 y 400 minutos, el precio es
    de 0.18$. Encima de 400 minutos, el precio por minuto es de 0.15$.
"""

minutos = int(input("Cuántos minutos Ud. utilizó este mes: "))
while minutos <= 0:
    minutos = int(input("Cuántos minutos Ud. utilizó este mes: "))

precio: float = 0
total_a_pagar: float = 0

if 0 < minutos < 200:
    precio = 0.20
    total_a_pagar = minutos*precio
else:
    if minutos < 400:
        precio = 0.18
        total_a_pagar = minutos * precio
    else:
        precio = 0.15
        total_a_pagar = minutos * precio

resultado = """
    Ud. va a pagar este mes: {0!s} $
""".format(total_a_pagar)

print(resultado)