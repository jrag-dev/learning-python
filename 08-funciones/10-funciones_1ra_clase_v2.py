"""
    Funciones de 1ra clase
"""

def create_adder(x):
    def adder(y):
        return x+y

    return adder


# main code
add_15 = create_adder(15)
print(add_15(10))