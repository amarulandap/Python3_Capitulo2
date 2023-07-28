"""Clase para implementar un iterador"""

class File:

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

""" 
if not hasattr(file, '__iter__'):
    raise TypeError('Debe ser un iterador')

iter = file.__iter__()

if not hasattr(iter, '__next__'):
    raise TypeError('Debe ser un iterador')

try:
    while True:
        res = iter.__next__()
        print(res)
except StopIteration:
    print('Termina')
    
      
class File1(Iterable):
    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
"""



