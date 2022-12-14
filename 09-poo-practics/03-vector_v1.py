"""
    Implementación de una clase vector que representa un vector en tres dimensiones
    y permite hacer sumas vectoriales y productos vectoriales.
"""


class Vector:
    def __init__(self, x, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def suma_vectorial(self, v):
        suma = Vector(self.__x + v.__x, self.__y + v.__y, self.__z + v.__z)
        return suma

    def multiplicacion_vectorial(self, v):
        xm = self.__y * v.__z - self.__z * v.__y
        ym = -self.__x * v.__z + self.__z * v.__x
        zm = self.__x * v.__y - self.__y * v.__x
        multiplicacion = Vector(xm, ym, zm)
        return multiplicacion

    def __eq__(self, otherV):
        if self.__x == otherV.__x and self.__y == otherV.__y and self.__z == otherV.__z:
            return True
        return False

    def __str__(self):
        return f"(x={self.__x}, y={self.__y}, z={self.__z})"


# main


if __name__ == '__main__':
    vector1 = Vector(1, 1, 1)
    vector2 = Vector(2, 2, 2)
    vector3 = Vector(3, 3, 3)
    vector4 = Vector(0, 0, 0)

    vectorResultAdd = vector1.suma_vectorial(vector2)
    print(vectorResultAdd)

    vectorResultMul = vector1.multiplicacion_vectorial(vector2)

    if vectorResultMul == vector3:
        print("addVectors Test Passed")
    if vectorResultMul == vector4:
        print("mulVectors Test Passed")