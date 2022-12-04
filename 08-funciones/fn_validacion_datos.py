"""
    Función que permite capturar un valor y validarlo
"""

def valida_input(pregunta, minimo, maximo):
    while True:
        v = int(input(pregunta))
        if v < minimo or v > maximo:
            print("Valor inválido. Digite un valor entre %d y %d" % (minimo, maximo))
        else:
            return v


entrada = valida_input("¿Cuál es el valor de a? ", 0, 10)

print(entrada)