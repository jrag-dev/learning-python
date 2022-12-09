"""
    Cuando se crean más de una clase derivada a partir de una única base, este
    tipo de herencia se denomina herencia jerárquica. En este programa, tenemos
    una clase principal (base) y dos clases secundarias (derivadas).
"""

class Parent:
    def func1(self):
        print("This function is in parent class.")


# primera clase derivada
class Child1(Parent):

    def func2(self):
        print("This function is in child 1")


# segunda clase derivada
class Child2(Parent):
    def func3(self):
        print("this function is in child 2.")


# main code
obj1 = Child1()
obj2 = Child2()

obj1.func1()
obj1.func2()

obj2.func1()
obj2.func3()
