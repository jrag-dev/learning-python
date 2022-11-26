"""
    Escribir un programa que encuentre todas las ocurrencias de una palabra si es que existe
    y la posición donde se encuentran
"""

t = "un tigre, dos tigres, se están comiendo a otro tigre. el otro tigre es como un gatito."

i = 0
while i > -1:
    i = t.find("tigre", i)
    if i >= 0:
        print("Posición: %d" % i)
        i += 1
