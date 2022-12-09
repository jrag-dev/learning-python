"""
    Argumentos de palabra clave de longitud variable
"""

def miFun(**kwargs):
    """Función que implementa un ejemplo del uso de los kwargs argumentos"""
    for key, value in kwargs.items():
        if key == "mid":
            print("Mid Item")
        print("%s == %s" % (key, value))


# main code
miFun(first="Geeks", mid="for", last="Geeks")
print(miFun.__doc__)