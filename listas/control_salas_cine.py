"""
    Programa que controla la utilización de las salas de cine.
"""

lugares_vacios = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Sala (o para salir): "))

    if sala == 0:
        print("Fin")
        break
    if sala > len(lugares_vacios) or sala < 1:
        print("Sala inválida")
    elif lugares_vacios[sala - 1] == 0:
        print("¡Disculpe, sala llena!")
    else:
        lugares = int(input("¿Cuántos lugares desea usted (%d vacios): " % lugares_vacios[sala-1]))

        if lugares > lugares_vacios[sala - 1]:
            print("Ese número de lugares no está disponible.")
        elif lugares < 0:
            print("Número inválido!")
        else:
            lugares_vacios[sala - 1] -= lugares
            print("%d lugares vendidos" % lugares)


print("Utilización de las salas.")

for x, l in enumerate(lugares_vacios):
    print("Sala %d - %d lugar(es) vacío(s)" % (x+1, l))