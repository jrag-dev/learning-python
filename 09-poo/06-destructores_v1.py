"""
    Destructors se llaman cuando un objeto se destruye. En Python, los
    destructores no se necesitan como en C++ porque python tiene un
    recolector de basura que maneja la administración de la memoria
    automaticamente.

    El método __del__() es conocido como destructor en Python. Se
    llama cuando han eliminado todas las referencias al objeto.
"""

class Employee:

    """ Inicialización """
    def __init__(self):
        print("Employee created.")

    # Eliminación (Llamada al destructor)
    def __del__(self):
        print("Destructor llamado, Employee eliminado.")


obj = Employee()
del obj