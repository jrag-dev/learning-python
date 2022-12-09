"""
    Uno de los conceptos centrales en los lenguajes de programación orientada a
    objetos (POO) es la herencia. Es un mecanismo que le permite crear una
    jerarquía de clases que comparten un conjunto de propiedades y métodos al
    derivar una clase de otra clase. La herencia es la capacidad de una clase para
    derivar o heredar las propiedades de otra clase.
"""

class Person(object):

    """ Constructor """
    def __init__(self, name, dni):
        self.name = name
        self.dni = dni

    # Para chequear si esta persona es un employee
    def display(self):
        print(self.name, self.dni)


# main code
emp = Person("Jose Alvarado", 102)
emp.display()

""" 
    Emp es otra clase que va a heredar las propiedades de la clase Person (clase base)
"""

class Emp(Person):

    def printer(self):
        print("Llamada a la clase Emp")


Emp_details = Emp("Mayank", 130)

# Llamando a la función de la clase padre
Emp_details.display()

# Llamando a la función de la clase hijo
Emp_details.printer()