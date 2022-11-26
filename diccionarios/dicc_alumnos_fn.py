"""
    Dada una lista de alumnos llamada lista_alumnos, donde cada elemento corresponde a un string
    con el número de alumno y nombre, separados por un guión (por ejemplo, '123-Juan'). Crea
    una función que reciba dicha lista y retorne un diccionario cuyas llaves correspondan al número
    de alumno y los valores al respectivo nombre del alumno. Luego imprime cada elemento
    del diccionario de la siguiente forma; "key: value"
"""

def listaToDict(lista):
    dicc = {}
    for elemento in lista:
        numero_nombre = elemento.split("-")
        numero = int(numero_nombre[0])
        nombre = numero_nombre[1]
        dicc[numero] = nombre
    return dicc


lista_alumnos = ["123-Juan", "124-Karla", "125-Veronica", "126-Paola"]

print("\nMostrando los datos: \n")
dicc_alumnos = listaToDict(lista_alumnos)
for item in list(dicc_alumnos.keys()):
    print("{}: {}".format(item, dicc_alumnos[item]))

print("\nOtra forma de mostrar los datos: \n")
for clave, valor in dicc_alumnos.items():
    print("{}: {}".format(clave, valor))