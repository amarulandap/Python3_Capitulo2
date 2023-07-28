"""Clase de práctica para el mecanismo de propiedades"""

class Boletin:

    def __init__(self, *notas):

        self.notas = list(notas)

    @property
    def media(self):
        if len(self.notas):
            return sum(self.notas) / len(self.notas)
        else:
            return 0

    @property
    def ultimaNota(self):
        if len(self.notas):
            return self.notas[-1]
        else:
            return None

    @ultimaNota.setter                              # Agregar una nota al final de la lista.
    def ultimaNota(self, nota):
        self.notas.append(nota)

    @ultimaNota.deleter                             # Eliminamos la última posición de la lista.
    def ultimaNota(self):
        self.notas.pop()

    # Lo que realizamos fue una sobrecarga del método ultimaNota.

