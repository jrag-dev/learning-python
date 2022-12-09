"""
    Los constructores se utilizan generalmente para instanciar un objeto. Estos
    inicializan (asignan valores) a los embroils de datos de la clase cuando se
    crea un objeto de la clase. En python, el método __init__() se llama
    constructor y siempre se llama cuando se crea un objeto.

    Tipos de constructores:
        1. constructor predeterminado: es un contructor simple que no acepta
        ningún argumento. Su definición tiene un solo argumento que es una
        referencia a la instancia que se está construyendo.

        2. constructor parametrizado: el constructor con parámetros se conoce
        como constructor parametrizado. Esté toma su primer argumento como una
        referencia a la instancia que se está construyendo conocida como self
        y el resto de los argumentos los proporciona el programador.
"""


class GeekforGeeks:

    """ constructor por default """
    def __init__(self):
        self.geek = "GeekforGeeks"

    # un método para imprimir los miembros de la data
    def print_Geek(self):
        print(self.geek)


obj = GeekforGeeks()

obj.print_Geek()