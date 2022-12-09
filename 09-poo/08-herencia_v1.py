"""
    Ejemplo de aplicar herencia en Python
"""

class Person(object):

    """ Constructor """
    def __init__(self, name):
        self.name = name

    # Obtener el nombre
    def getName(self):
        return self.name

    # Chequear si esta persona es un employee
    def isEmployee(self):
        return False


# Subclase ( hereda de Person)
class Employee(Person):

    """ Aqui retornamos True (Sobrecarga de métodos en java) """
    def isEmployee(self):
        return True


# main code
emp = Person("Jose Alvarado")
print(emp.getName(), emp.isEmployee())

emp = Employee("Paola Rodriguez")
print(emp.getName(), emp.isEmployee())