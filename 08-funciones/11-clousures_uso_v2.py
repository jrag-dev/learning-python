"""
    Un Closure es un objeto de función que recuerda valores en ámbitos adjuntos
    incluso si no están presentes en la memoria.
"""

def outerFunction(text):

    def innerFunction():
        print(text)

    return innerFunction


# main code
if __name__ == '__main__':
    word = "José Alvarado"
    myFunction = outerFunction(word)
    myFunction()