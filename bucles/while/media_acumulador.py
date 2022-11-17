x = 1
suma = 0

while x <= 5:
    n = int(input("%d Digite el número: " % x))
    suma = suma + n
    x = x + 1

print("Media: %5.2f" % (suma/5))