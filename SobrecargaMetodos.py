"""Programa para probar la sobrecarga de métodos en Python"""

from Herencias import Punto1D
from functools import singledispatch
# Singledispatch me permite declarar funciones que reciben parámetros sin necesidad de conocer el tipo.

@singledispatch
def funcionUno(arg):
    print('Comportamiento por defecto.')

@funcionUno.register(int)
@funcionUno.register(float)
def _(arg):
    print('Comportamiento para un número')

@funcionUno.register(Punto1D)
def _(arg):
    print('Comportamiento para un punto en una sola dimensión.')



