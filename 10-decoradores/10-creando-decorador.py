"""
    Creando decoradores

    decorador sencillo que convierte una oración a mayúsculas. Esto se
    realiza definiendo un contenedor dentro de una función que lo envuelve,
    esto es muy similar a una función dentro de otra función.
"""

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'


print(say_hi())