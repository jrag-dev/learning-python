"""
    Función rectangulo con parámetros obligatorios y opcionales
"""


def rectangulo(ancho, altura, carácter="*"):
    linea = carácter * ancho
    for i in range(altura):
        print(linea)


rectangulo(9, 10, "'")
