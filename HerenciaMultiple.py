"""Programa para observar el como se implementa la herencia multiple en Python"""

from Herencias import Punto2D

class Edificio():

    def __init__(self, nombre, recursos):
        self.nombre = nombre
        self.recursos = recursos


    def producir(self):

        return "El edificio {} produce {}".format(self.nombre, self.recursos)


class EdificioUnico(Edificio, Punto2D):

    def __init__(self, nombre, recursos, x, y):     # Recibir los parámetros correspondientes a todos los atributos.
        super().__init__(x, y)
        super().__init__(nombre, recursos)





