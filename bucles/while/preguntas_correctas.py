

puntos = 0
pregunta = 1

while pregunta <= 3:
    respuesta = input("Respuesta de la pregunta %d: " % pregunta)

    if pregunta == 1 and respuesta == "b":
        puntos = puntos + 1
    if pregunta == 2 and respuesta == "a":
        puntos = puntos + 1
    if pregunta == 3 and respuesta == "d":
        puntos = puntos + 1
    pregunta += 1

print("El alumno hizo %d punto(s)" % puntos)