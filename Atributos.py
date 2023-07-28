"""Mirar los diferentes niveles de provacidad de los atributos"""

class Ejemplo:


    x = ''
    y = ''
    z = ''
    read_only = ['x', 'y']           # Lista que indica que X y Y son de solo lectura.


    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __setattr__(self, key, value):                  #Asignar valor al atributo.
        if key in self.read_only:
            raise Exception('Atributo de solo lectura')
        else:
            return object.__setattr__(self, key, value)

    def __delattr__(self, item):                        #Eliminar el atributo.
        if item in self.read_only:
            raise Exception('Atributo de solo lectura')
        else:
            return object.__setattr__(self, item)






