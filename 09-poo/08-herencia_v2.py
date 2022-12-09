"""
    Constructor de llamadas de la clase principal
"""


class Person(object):
    """ __init__ es conocido como constructor """

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# Clase hija

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invocamos el constructor __init__() se la clase padre
        Person.__init__(self, name, idnumber)


# creación de una instancia de employee
a = Employee("José", 886012, 2000, "Inter")

# llamada al método display de la clase Person, que fue heredado en Employee
a.display()

print(a)