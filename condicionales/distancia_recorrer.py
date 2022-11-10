"""
    Escriba un programa que pregunte la distancia que un pasajero desea recorrer
    en kms. Calcule el precio del pasaje, cobrando 0.50$ por km para viajes de
    hasta 200km y 0.45 para más largos.
"""

precio_pasaje = 0
precio_final = 0

distancia = float(input("Ingresa la distancia a recorrer: "))
edad = int(input("Ingrese la edad del pasajero: "))

while edad < 0 or edad > 100:
    edad = int(input("Ingrese la edad del pasajero: "))

if distancia <= 200:
    precio_pasaje = distancia*0.50
else:
    precio_pasaje = distancia*0.45

if edad > 55:
    precio_final = precio_pasaje*0.50
elif 0 < edad < 5:
    precio_final = 0
else:
    precio_final = precio_pasaje

resultado = """
    Distancia a recorrer: {0!s} km
    Precio del pasaje: {1!s} $
""".format(distancia, precio_final)

print(resultado)