"""
    Programa que muestra el uso de *args con un primer argumento extra
"""

def myFun(arg1, *argv):
    print("Primer argumento: ", arg1)
    for arg in argv:
        print("Próximo argumento a través de *argv: ", arg)


# main code
myFun("Hello", "Welcome", "to", "GeeksforGeeks")