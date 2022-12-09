"""
    Implementación de una función que recibe dos enteros y calcula su suma
"""

def add(number1: int, number2: int) -> int:
    """ Add two numbers"""
    num3 = number1 + number2
    return num3


# main code
num1, num2 = 5, 15
sol = add(num1, num2)
print(f"The addition of {num1} and {num2} results {sol}.")