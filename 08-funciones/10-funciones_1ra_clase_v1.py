"""
    Funciones de primera clase:

    1. Las funciones son objetos.
    2. Se pueden pasar como parámetros a otras funciones
"""

def shout(text):
    return text.upper()


print(shout("Hello"))

yell = shout

print(yell("World"))

print("\n**********************************************************\n")

def whisper(text):
    return text.lower()


def greet(func):
    """almacena la función en una variable"""
    greeting = func("""Hi, I am created by a function passed as a argument.""")
    print(greeting)


greet(shout)
greet(whisper)