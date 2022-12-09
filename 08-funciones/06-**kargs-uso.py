"""
    La sintaxis especial **kwargs en las definiciones de funciones en python
    se usa para pasar una lista de argumentos de longitud variable con palabras
    clave.
"""

def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# main code
myFun("Hi", first="jose", last="Alvarado", age=34, profession="Backend Developer")