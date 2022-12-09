"""
    Implementación de una función anónima, también llamadas funciones lambda.
"""

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

for i in range(1, 21):
    x = calc(i)
    print(x)
