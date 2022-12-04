"""
    Escribir un programa que genere un diccionario donde cada clave sea un caráter, y su
    valor sea el número de ese carácter encontrado en una frase leída.

    Ejemplo:
    hola mundo desde python ->
    {'h': 2, 'o': 3, 'lo': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 2, 'd': 3, 'e': 2, 's': 1, 'p': 1, 'y': 1, 't': 1}
"""

frase = input("Ingrese un frase: ")

lista_frase = []
for item in frase:
    if item != " ":
        lista_frase.append(item)

dicc = {}
for item in lista_frase:
    if item in dicc:
        print(item)
        dicc[item] += 1
    else:
        dicc[item] = 1

print(dicc)