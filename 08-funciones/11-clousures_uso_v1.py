"""
    Antes de ver que son las clousures, veamos que fon funciones anidadas.

    Una función anidada que se define dentro de otra función se conoce como
    función anidada. Las funciones anidadas pueden acceder a las variables
    del ámbito adjunto.

    En Python, solo se puede acceder a estas variables no locales dentro
    de su alcance y no fuera de su alcance.
"""

def outerFunction(text):

    def innerFunction():
        print(text)

    innerFunction()


# main code
if __name__ == '__main__':
    outerFunction('Hey!')