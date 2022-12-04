"""
    Para sustituir tramos de una cadena de caracteres por otros, se puede utilizar el
    método replace.
"""

s = "un tigre, dos tigres, tres tigres"

felino = s.replace("tigre", "gato")
print(felino)

# sustituir n conincidencias
gato_1 = s.replace("tigre", "gato", 1)
print(gato_1)

lenguaje = "python"
nombre = "ot"
cadena = ""

i = 0
k = 0
while i < len(lenguaje):
    for j in nombre:
        if lenguaje[i] == j:
            k += 1
            cadena = lenguaje.replace(lenguaje[i], "-", k)
            print("{} : {} => iguales".format(lenguaje[i], j))
            print(lenguaje, j)
        else:
            print("{} : {} => diferentes".format(lenguaje[i], j))
    i += 1

print(cadena)
