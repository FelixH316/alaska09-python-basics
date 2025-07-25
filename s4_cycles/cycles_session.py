# *********************************************************
# COURSE 09 SESSION 04
# *********************************************************

"""
ESTRUCTURAS DE REPETICIÓN
Cuando tenemos que ejecutar un mismo bloque de comandos durante varias
    ocasiones no es nada práctico hacerlo a mano.

SITUATION 05
Nos fue solicitado obtener e imprimir el promedio de 2 notas de 3 estudantes:
"""
nota_1 = float(input("Digita la primera nota: "))
nota_2 = float(input("Digita la segunda nota: "))
print(f"\tEl promedio del estudiante 1 es: {(nota_1 + nota_2) / 2}")

nota_1 = float(input("Digita la primera nota: "))
nota_2 = float(input("Digita la segunda nota: "))
print(f"\tEl promedio del estudiante 2 es: {(nota_1 + nota_2) / 2}")

nota_1 = float(input("Digita la primera nota: "))
nota_2 = float(input("Digita la segunda nota: "))
print(f"\tEl promedio del estudiante 3 es: {(nota_1 + nota_2) / 2}")

"""
Ahora imaginemos una situación en que no son tan solo 3 estudiantes, sino 100 estudiantes. No sería nada interesante repetir el mismo código 100 veces, sino ejecutar el mismo código 100 veces.

¡Esta estructura la logramos construir con lazos de repetición!

WHILE

El lazo while es una estructura de control de repetición en Python que permite ejecutar un bloque de código repetidamente mientras que una determinada condición sea verdadera. Su estructura es:

while condicion:
    # bloque de codigo
Vamos a construir un ejemplo con un contador de 1 hasta 10.
"""

# Ahora vamos a colectar las notas y promedios de cada alumno dentro del lazo while. Haremos un ejemplo con 3 promedios.

"""
El lazo for es un tipo de estructura de control de flujo en Python que permite iterar sobre un conjunto de elementos. Su estructura es:

for elemento in conjunto:
    # codigo a ser ejecutado para cada elemento
El lazo for itera sobre cada elemento del conjunto especificado y ejecuta el bloque de código dentro del lazo para cada elemento. Cuando el lazo llega al final del conjunto, este se interrumpe y el programa continúa la ejecución después del lazo.

El conjunto lo podemos generar con la función incorporada range(). Se trata de una función capaz de generar una secuencia de números enteros. La estructura de esta función es:

range(inicio, fin, paso)
Según la documentación, range() genera una secuencia de números enteros a partir del valor del parámetro inicio hasta el valor del parámetro fin, de acuerdo con el valor del parámetro paso. Si inicio no es especificado, el valor por defecto es 0. Si paso no es especificado, el valor por defecto es 1.

Vamos a recrear el mismo contador while con el lazo for.
"""