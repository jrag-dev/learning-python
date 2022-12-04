"""
    Función que implementa la secuencia de fibonacci
"""

fibo = {}
def fibonacci(n):
    if n <= 1:
        print("Secuencia de fibonacci de %d" % n)
        fibo[n] = n
        return n
    else:
        fib = fibonacci(n - 1) + fibonacci(n - 2)
        fibo[n] = fib
        print("Secuencia de fibonacci de %d = %d" % (n, fib))
        return fib


print(fibonacci(8))
print(fibo)