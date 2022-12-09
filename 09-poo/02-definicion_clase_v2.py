"""
    Aquí aprenderemos sobre el método __init__, esté se utiliza para inicializar el
    estado del objeto.
"""


class Person:
    """ *** método init o constructor *** """
    def __init__(self, name):
        self.name = name

    # método de muestra
    def saludo(self):
        print('Hello, my name is', self.name)


p = Person("José Alvarado")
p.saludo()