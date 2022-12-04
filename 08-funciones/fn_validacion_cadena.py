"""
    Escribir una función para validar una variable, cadena de caracteres. Esa función
    recibe como parámetro la cadena de caracteres, el número minimo y máximo de caracteres.
    Retorne verdadero si el tamaño de la cadena de caracteres esta dentro del rango, y
    falso en caso contrario.
"""


def validar_cadena(cadena, minimo, maximo):
    l = len(cadena)
    if l < minimo or l > maximo:
        return False
    else:
        return True


es_valida = validar_cadena("hola mundo, python", 4, 20)

print(es_valida)
