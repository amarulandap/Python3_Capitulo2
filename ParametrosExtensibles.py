"""Programa de prueba del funcionamiento de los parámetros extensibles"""

def pruebaExtensibles (a, b=0, *args, **kwargs):

    print("\nNombrados: ", kwargs.values())           # Imprimir los valores contenidos por el diccionario.
    print("No nombrados: ", args)                     # Imprimir los valores contenidos en la tupla.
    return a + b + sum(args) + sum(kwargs.values())

# Los argumentos no nombrados son aquellos a los cuales no se les asigna un identificador.

"""Los argumentos extensibles me dan la posibilidad de llamar a una función incluyendo 
    o no todos los parámetros nombrados o no nombrados"""

suma = pruebaExtensibles(2, 1, 2, 3, x=1, y=2)
print("\nsuma =", suma)
suma1 = pruebaExtensibles(3, 10)
print("\nsuma1 =", suma1)


# Anotaciones.
# Informar al usuario el tipo de dato de cada uno de los parámetros de la función, y del valor retornado.

def pruebaAnotaciones (a:str, b:int)->int:

    print(" ")
    print(locals())
    return 5

print("Prueba con valores enteros: ",pruebaAnotaciones(2, 7))
print("Prueba con valores string y entero: ",pruebaAnotaciones("Hola, soy una anotación", 56))
