"""
    La herencia única permite que una clase derivada herede propiedades de una sola
    clase principal, lo que permite la reutilización de código y la adición de
    nuevas caracteristicas al código existente.
"""

class Parent:
    def func1(self):
        print("Esta función esta en la clase padre")


class Child(Parent):
    def func2(self):
        print("Esta función esta en la clase hija")


# main code
obj = Child()
obj.func1()
obj.func2()
