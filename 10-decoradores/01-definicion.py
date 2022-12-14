"""
    Los decoradores son una herramienta muy poderosa y útil en Python ya que permite a
    los programadores modificar el comportamiento de una función o clase. Los decoradores
    nos permiten envolver otra función para extender el comportamiento de la función
    envuelta, sin modificarla permanentemente.
"""

def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")

        # llamada a la función que se pasa como parámetro
        func()

        print("This is after function execution")

    return inner1


def function_to_be_used():
    print("This is inside the function !!")


# pasando "function_to_be_used" dentro del decorador para controlar su comportamiento
function_to_be_used = hello_decorator(function_to_be_used)

# llamando a la función
function_to_be_used()