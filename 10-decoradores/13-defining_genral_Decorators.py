"""
    Definiendo decoradores de propósito general

   Para definir un decorador de propósito general que puede ser aplicado a cualquier
   función se usan args y **kwargs.

   Estos recopilan todos los argumentos posicionales y de palabras clave y los almacenan
   en las variables args y kwargs. Estos nos permiten pasar tantos argumentos como
   queramos durante las llamadas a las funciones.
"""

def a_decorador_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('Los argumentos posicionales son: ', args)
        print('Los argumentos de palabras claves son: ', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments


@a_decorador_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here")


@a_decorador_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


@a_decorador_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print('This has shown keyword arguments')


function_with_no_argument()
function_with_arguments(1, 2, 3)
function_with_keyword_arguments(first_name="José", last_name="Alvarado")