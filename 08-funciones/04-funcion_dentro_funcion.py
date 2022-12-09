"""
    Una función que se define dentro de otra función se conoce como función interna
    o función anidada. Las funciones anidadas pueden acceder a las variables del
    ámbito adjunto.

    Las funciones internas se utilizan para que puedan protegerse de todo lo que
    sucede fuera de la función.
"""

def f1():
    s = "I'm a Backend Developer in Cumaná"

    def f2():
        print(s)

    f2()


# main code
f1()