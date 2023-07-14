"""Crear tres clases, una clase madre y dos hijas que hereden el método para el calculo de la distancia entre los puntos"""

import math
from functools import singledispatch

class Punto3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calcularDistanciaEntrePuntos(self, other):

        distancia = math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2) + math.pow(self.z - other.z, 2))

        return distancia

    def convertirATupla(self):

        return (self.x, self.y, self.z)

class Punto2D(Punto3D):

    def __init__(self, x, y):
        super().__init__(x, y, 0)

    """def convertirATupla(self):
            # assert self.z == 0
            return super().convertirATupla()"""

class Punto1D(Punto2D):

    def __init__(self, x):
        super().__init__(x, 0)







