"""
    Aplicando multiples decoradores a una función sencilla
"""

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string
@uppercase_decorator
def say_hi():
    return "Aprendiendo decoradores en Python"


print(say_hi())