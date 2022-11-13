"""
    Escriba un programa que calcule el precio a pagar por el suministro de energía
    eléctrica. Pregunte la cantidad de kwh consumida y el tipo de instalación:
    R => para residencias
    I => para industrias
    C => Comercios
    Calcule el precio a pagar de acuerdo con los siguientes datos
    Resisencial => hasta 500 kwh 0.40$ => mas de 500 kwh 0.65$
    Comercial => hasta 1000 kwh 0.55 $ => más de 1000 kwh 0.60
    Insdustrial => hasta 5000 kwh 0.55 $ => más de 5000 kwh 0.60
"""

kwh_mes = 0.0

def menu():
    opciones = """
      ***************************************************
      | Factura por el suministro de Energía Eléctrica. |
      ***************************************************
      
        Debe indicar tipo de instalación:
        Residencial: 1
        Comercial:   2
        Industrial:  3
    """
    print(opciones)


def suministro_precio(opcion, cantidad):
    precio_a_pagar = 0.0

    if opcion == 1:
        tipo = "residencial"
        if cantidad < 500:
            precio_a_pagar = 0.40*cantidad
        else:
            precio_a_pagar = 0.65 * cantidad

    elif opcion == 2:
        tipo = "comercial"
        if cantidad < 1000:
            precio_a_pagar = 0.55*cantidad
        else:
            precio_a_pagar = 0.60 * cantidad

    elif opcion == 3:
        tipo = "industrial"
        if cantidad < 5000:
            precio_a_pagar = 0.55*cantidad
        else:
            precio_a_pagar = 0.60 * cantidad

    else:
        tipo = "Incorrecto!!"

    return precio_a_pagar, tipo

def toString(precio, tipo, cantidad):
    sheet = """
        Tipo de Instalación: {0!s}
        Cantidad de Kwh por mes: {1!s}
        Precio a Pagar: {2!s} $
    """.format(tipo, cantidad, precio)
    print(sheet)


def main():
    menu()

    opcion = int(input("Tipo de instalación: "))

    while opcion < 0 or opcion > 4:
        opcion = int(input("Tipo de instalación: "))

    cantidad = float(input("Ingrese la cantidad de kwh por mes: "))
    while cantidad < 0:
        cantidad = float(input("Ingrese la cantidad de kwh por mes: "))

    total_a_pagar, tipo = suministro_precio(opcion, cantidad)

    toString(total_a_pagar, tipo, cantidad)


main()




