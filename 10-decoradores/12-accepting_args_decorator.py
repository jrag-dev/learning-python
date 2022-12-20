"""
    Aceptando argumentos en funciones decoradoras
"""

def decorator_with_arguments(function):
    def wrapper(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)

    return wrapper


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))


cities("Carupano", "Madrid")