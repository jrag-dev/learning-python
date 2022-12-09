"""
    Implementación del uso de los *argv y los **kwargs
"""

def myFun(*argv, **kwargs):
    print("args: ", argv)
    print("kwargs: ", kwargs)


# main code
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")