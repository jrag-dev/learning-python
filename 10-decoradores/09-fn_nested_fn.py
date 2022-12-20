"""
    Funciones anidadas tiene acceso a las varibles del ámbito de la función envolvente
"""

def print_message(message):
    """ Función envolvente """
    def message_sender():
        """ Función anidada """
        print(message)

    message_sender()


print_message("Aprendiendo decoradores")