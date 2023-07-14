"""Clase declarada de manera imperativa"""

class DePrueba:

    # Atributos.
    atributoUno = 0                         # Debo incializar los atributos para indicar el tipo de dato.
    atributoDos = "Esto es un atributo."
    atributoTres = 0                           # Atributo de clase.

    # Método constructor.
    def __init__(self, atributoUno, atributoDos):
        self.atributoUno = atributoUno
        self.atributoDos = atributoDos
        self.contarObjetos()                # Invocar el método de clase.

    # En Python no son necesarios los métodos get, ya que se puede acceder a los valores de los atributos usando la notación punto.

    # Con la palabra self indico que es una instancia la que está accediendo al valor del atributo o invocando el método.

    # Set atributo dos
    def setAtributoDos(self, atributoDos):
        self.atributoDos = atributoDos


    # Set atributo uno.
    def setAtributoUno(self, atributoUno):
        self.atributoUno = atributoUno

    # Método de clase
    @classmethod
    def contarObjetos(cls):
        cls.atributoTres += 1
        return cls.atributoTres

    # Método de instancia.
    # Todos los métodos de instancia, incluido el constructor llevarán el parámetro self.
    def metodo1(self, *args, **kwargs):
        return "Hola, soy el método 1."


    """def distanciaRespectoAlOrigen(self):
        La distancia respecto al origen es igual a la raíz cuadrada de la suma de los cuadrados de las coordenadas

        modulo = math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

        return modulo
        
    def distanciaEntrePuntos(self, other):
        la distancia entre dos puntos

        distancia = math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2) + pow(self.z - other.z, 2))

        return distancia"""

