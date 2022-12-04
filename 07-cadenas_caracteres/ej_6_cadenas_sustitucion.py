"""
    EScriba un programa que lea tres cadenas de caracteres. Imprima el resultado de la sustitución
    en la primera, de los caracteres de la segunda por los de la tercera.

    1ra cadena de caracteres => AATTCGAA
    2da cadena de caracteres => TG
    3ra cadena de caracteres => AC

    Resultado => AAAACCAA
"""

primera_cadena = "PQWPSTWQ"
segunda_cadena = "QW"
tercera_cadena = "CA"
resultado = []

indices = []
i = 0
while i < len(primera_cadena):
    for j in segunda_cadena:
        if primera_cadena[i] == j:
            indices.append(i)
    i += 1

l1 = list(primera_cadena)
l2 = list(segunda_cadena)
j = 0
while j < len(l1):
    k = 0
    while k < len(tercera_cadena):
        if j in indices:
            n = 0
            if n == k and n <= len(l2):
                l2[n] = tercera_cadena[k]
                l1[j] = l2[n]
                print("l2[%s] = %s" % (n, l2[n]))
                print("l1[%s] = %s" % (j, l1[j]))
                n += 1
        k += 1
    j += 1

print(l1)