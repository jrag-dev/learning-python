"""
    Reutilización de una función dentro de otra función
"""

def espar(x):
    return x%2 == 0

def par_o_impar(x):
    if espar(x):
        return "par"
    else:
        return "impar"


print(par_o_impar(8))
print(par_o_impar(9))