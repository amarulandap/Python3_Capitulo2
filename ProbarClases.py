"""Programa para probar algunas de las clases creadas en la unidad"""

# Probar la clase de prueba.
from ClaseDePrueba import DePrueba
import Herencias
import SobrecargaMetodos
import HerenciaMultiple

objeto1 = DePrueba(10, "Hola, soy el objeto número")             # Creamos el primer objeto.
print(objeto1.atributoDos, DePrueba.atributoTres)                # Imprimimos el valor de los atributos usando la notación punto.
print(objeto1.metodo1())
print("valor del atributo uno:", objeto1.atributoUno)
objeto2 = DePrueba(15, "Hola, soy el objeto número")             # Creamos el segundo objeto.
print(objeto2.atributoDos, DePrueba.atributoTres)                # Validamos el funcionamiento del atributo y el método de clase.
objeto1.setAtributoUno(20)                                       # Modificar el valor del primer atributo en ambos objetos.
objeto2.setAtributoUno(25)
print(objeto1.atributoUno, objeto2.atributoUno)                  # Invocar el método getattr con cada objeto.

# Probar la clase Herencias.
punto1_3d = Herencias.Punto3D(2, 5, 7)
punto2_3d = Herencias.Punto3D(4, 10, 6)
print("\nDistancia entre los dos puntos:", punto1_3d.calcularDistanciaEntrePuntos(punto2_3d))

print("\nTupla con los elementos del punto1:", punto1_3d.convertirATupla())

punto1_2d = Herencias.Punto2D(12, 8)
punto2_2d = Herencias.Punto2D(6, 4)
print("\nDistancia entre los puntos 2D es:", punto1_2d.calcularDistanciaEntrePuntos(punto2_2d))

print("\nTupla con los elementos del punto1 en 2D:", punto1_2d.convertirATupla())

punto1_1d = Herencias.Punto1D(10)
punto2_1d = Herencias.Punto1D(5)
print("\nDistancia entre los puntos en el eje x es:", punto1_1d.calcularDistanciaEntrePuntos(punto2_1d))

print("\n")
SobrecargaMetodos.funcionUno('Andres')
SobrecargaMetodos.funcionUno(10)
SobrecargaMetodos.funcionUno(20.47)
SobrecargaMetodos.funcionUno(Herencias.Punto1D(10))

print("\n")
edificio1 = HerenciaMultiple.EdificioUnico("Torre Lucía", ["Oro", "Plata", "Bronce"], 10, 20)
print(edificio1.producir())





