"""
    En python, podemos pasar un número variable de argumentos a una función usando
    simbolos especiales. Hay dos simbolos especiales:

    1. *argv => argumentos que no son palabras claves

    2. **kwargs => argumentos de palabras clave
"""

def myFun(*argv):
    for arg in argv:
        print(arg)


# main code
myFun("Hello", "Welcome", "to", "GeeksforGeeks")