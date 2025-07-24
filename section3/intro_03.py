# *********************************************************
# CLASS 01 SECTION 03
# *********************************************************

"""
ESTRUCTURAS CONDICIONALES
Los comandos if y else son dos estructuras condicionales. El comando if
    ejecutará el bloque de comandos en caso de que la condición citada
    sea verdadera. El comando else ejecutará el bloque de comandos en 
    el caso de que la condicional de if sea falsa.

El comando if es una palabra clave en Python que significa "si". Este 
    se emplea para conformar la estructura condicional, que te permite
    verificar si una determinada condición es verdadera o falsa e, 
    inmediatamente después, ejecute un bloque de código específico 
    dependiendo del resultado de la verificación. La sintaxis para usar
    el comando if es:

if condicion:
    # Realiza algo
"""
if 2 < 7:
    print("La condición es verdadera")

if 2 > 7:
    print("La condición es verdadera")
print("Fin de la consulta")

"""
Ya el comando else en Python se usa en junción con la palabra clave if
    para formar una estructura condicional. la sintaxis para usar el 
    else es:

if condicion:
  # codigo en caso de que sea verdad
else:
  # codigo en caso de que sea falso
el comando else se ejecuta cuando la condición verificada por el if es evaluada como False.
"""

if 2 > 7:
    print("La condición es verdadera")
else:
    print("La condición es falsa")
print("Fin de la consulta")


""" OPERADORES BOOLEANOS """
# Mayor que '>'
edad_maria = int(input('Ingrese la edad de María: '))
edad_beatriz = int(input('Ingrese la edad de Beatriz: '))

if edad_maria > edad_beatriz:
    print('María es mayor que Beatriz.')

# Menor que '<'
edad_maria = int(input('Ingrese la edad de María: '))
edad_beatriz = int(input('Ingrese la edad de Beatriz: '))

if edad_maria < edad_beatriz:
    print('María es menor que Beatriz')

# Mayor o igual que ">="
empleados_empresa_1 = int(input('Ingrese la cantidad de empleados de la empresa 1: '))
empleados_empresa_2 = int(input('Ingrese la cantidad de empleados de la empresa 2: '))

if empleados_empresa_1 >= empleados_empresa_2:
    print('La empresa 1 tiene una cantidad de empleados mayor o igual a la empresa 2.')

# Menor o igual que "<="
empleados_empresa_1 = int(input('Ingrese la cantidad de empleados de la empresa 1: '))
empleados_empresa_2 = int(input('Ingrese la cantidad de empleados de la empresa 2: '))

if empleados_empresa_1 <= empleados_empresa_2:
    print('La empresa 1 tiene una cantidad de empleados menor o igual a la empresa 2.')

# Igual a "=="
libro_1 = input('Ingrese el título del 1° libro: ')
libro_2 = input('Ingrese el título del 2° libro: ')

if libro_1 == libro_2:
    print('Los libros tienen el mismo título.')

# Diferente de "!="
libro_1 = input('Ingrese el título del 1° libro: ')
libro_2 = input('Ingrese el título del 2° libro: ')

if libro_1 != libro_2:
    print('Los libros tienen títulos diferentes.')


"""
SITUATION 03
Recibiremos el promedio de la nota de los estudiantes y necesitamos de
    un algoritmo que ejecute el análisis y determine si el estudiante 
    fue Aprobado o Reprobado, mostrando un mensaje del resultado. Para
    ser aprobado, el promedio necesita ser igual o superior a 7.0
"""

nota = float(input("\nDigita la nota: "))
if nota >= 7:
    print("\tAprobó")
else:
    print("\tReprobó")

# Ahora, nuestra institución educativa estableció que las personas que
#   tengan el promedio entre 5.0 y 7.0 pueden participar del curso de
#   Recuperación durante las vacaciones para lograr aprobar.
# Entonces podemos apoyarnos en un conjunto de ifs para poder 
#   estructurar esta nueva condición. Por ejemplo:
nota = float(input("\nDigita la nota: "))
if nota >= 7:
    print("\tAprobó")
if 7 > nota >= 5:
    print("\tRecuperación")
if nota < 5:
    print("\tReprobó")

# Observa que en casos con 3 situaciones como este necesitamos definir
#   bien nuestras condiciones. Pues, si realizamos una condición con 
#   else al final, este irá a considerar solamente la condición if 
#   inmediatamente anterior para generar la salida en caso de que el
#   resultado de su operación lógica sea falso dando como resultado, 
#   dos o más ejecuciones.
nota = float(input("\nDigita la nota: "))
if nota >= 7:
    print("\tAprobó")
if 7 > nota >= 5:               # Error porque 8 es valido para ambos
    print("\tRecuperación")
else:
    print("\tReprobó")


"""
ELIF
El comando elif es una palabra clave en Python que significa "si no, si"
    y lo podemos considerar una contracción entre else e if. Se utiliza
    en conjunto con la palabra clave if para formar una estructura 
    condicional en cadena.

La sintaxis para utilizar el comando elif es:
    if condicion1:
        # Realiza algo
    elif condicion2:
        # Realiza otra cosa
    elif condicion3:
        # Realiza otra cosa
    else:
        # Realiza algo diferente

El comando elif permite que puedas verificar varias condiciones en
    cadena, economizando espacio en tu código. Si la primera condición
    se evalúa como False, el interpretador de Python evaluará la 
    próxima condición con el elif. Ello continuará hasta que una
    condición sea evaluada como True o hasta que el else sea alcazado.
    Si ninguna de las condiciones es evaluada como True, la ejecución
    del código del comando else será iniciada.

Vamos a emplear el mismo caso anterior:
"""
print("\nCODIGO SIN ERRORES")
nota = float(input("\nDigita la nota: "))
if nota >= 7:
    print("\tAprobó")
elif 7 > nota >= 5:               # Error porque 8 es valido para ambos
    print("\tRecuperación")
else:
    print("\tReprobó")

"""
OPERADORES DE PYTHON
Durante la construcción de comandos a veces necesitamos de una
    elaboración mayor de la expresión condicional, necesitando que
    algunos operadores lógicos se encuentren integrados.

    AND, OR, NOT

Los operadores lógicos and, or y not son usados para combinar
    expresiones lógicas en Python. Ellos son usados frecuentemente en
    conjunto con el comando if para crear estructuras condicionales más
    complejas.

AND es usado para verificar si dos condiciones son verdaderas. La
    expresión lógica¹ x and y se evalúa como True tan solo si ambas
    condiciones x y y son verdaderas, y como False en caso contrario.

OR es usado para verificar si al menos una de las condiciones es
    verdadera. La expresión lógica x or y se evalúa como True si al
    menos una de las condiciones x o y es verdadera, y como False si
    ambas condiciones son falsas.

NOT es usado para negar una condición. La expresión lógica not x es
    evaluada como True si la condición x es falsa, y como False si la
    condición x es verdadera.

¹ Una expresión lógica es una declaración que puede ser evaluada como
    verdadera o falsa. Ella se compone por operandos lógicos² y por
    operadores lógicos³, que son usados ​​para combinar varias
    expresiones lógicas en una única expresión.

² Los operandos lógicos son los elementos que son comparados o
    evaluados en una expresión lógica. Ellos son generalmente valores
    verdaderos o falsos, pero también pueden ser expresiones lógicas
    más complejas. En Python, los operandos lógicos son los valores
    True y False.

³ Los operadores lógicos son ls símbolos o palabras clave que son
    usados ​​para combinar varias expresiones lógicas en una única
    expresión. En Python, los operadores lógicos son and, or y not,
    bien como las palabras clave if, elif e else.
__________________________
| a | b | AND | OR | NOT |
| 0 | 0 | 0   | 0  | 11  |
| 0 | 1 | 0   | 1  | 10  |
| 1 | 0 | 0   | 1  | 01  |
| 1 | 1 | 1   | 1  | 00  |
"""
v = True
f = False

# AND
if v and v:
    print("\tLa condición es verdadera")
else:
    print("\tLa condición es falsa")

# OR
if v or v:
    print("\tLa condición es verdadera")
else:
    print("\tLa condición es falsa")

# NOT
if not v:
    print("\tLa condición es verdadera")
else:
    print("\tLa condición es falsa")

"""
IN
Es usado para verificar si un elemento está presente en una lista,
    tupla u otra colección de conjunto. La expresión x in y se evalúa
    como True si el elemento x esta presente na variávelen la variable
    de conjunto y, y como False en caso contrario.

Podemos verificarlo con variables de texto.

SITUATION 04
En la escuela nos entregaron una lista con nombres de estudiantes que fueron aprobados según el promedio del semestre, pero es necesario verificar si algunos nombres están en esa lista para confirmar que los datos estén correctos.

La lista distribuida puede ser observada a continuación:

lista = 'Juan Pérez, María González, Pedro Rodríguez, Ana López, Carlos Martínez,
    Laura Sánchez, José García, Elena Fernández, Luis Morales, Carmen Torres,
    David Ruiz, Isabel Ramírez, Javier Díaz, Sara Herrera, Miguel Castro,
    Patricia Ortega, Francisco Vargas, Marta Jiménez, Manuel Medina, Rosa Molina,
    Alejandro Silva, Silvia Ruiz, Andrés Torres, Natalia Soto, Diego Guerrero,
    Paula Ríos, Ricardo Navarro, Alicia Cordero, Carlos Vidal, Lorena Gómez'
Los nombres que necesitas verificar son los siguientes:

nombre_1 = 'Miguel Castro'
nombre_2 = 'Marcelo Noguera'
"""
lista = "Juan Pérez, María González, Pedro Rodríguez, Ana López, Carlos Martínez, \
    Laura Sánchez, José García, Elena Fernández, Luis Morales, Carmen Torres, \
    David Ruiz, Isabel Ramírez, Javier Díaz, Sara Herrera, Miguel Castro, \
    Patricia Ortega, Francisco Vargas, Marta Jiménez, Manuel Medina, Rosa Molina, \
    Alejandro Silva, Silvia Ruiz, Andrés Torres, Natalia Soto, Diego Guerrero, \
    Paula Ríos, Ricardo Navarro, Alicia Cordero, Carlos Vidal, Lorena Gómez"

nombre_1 = 'Miguel Castro'
nombre_2 = 'Marcelo Noguera'

if nombre_1 in lista:
    print(f"\n\t{nombre_1} esta en la lista")
else:
    print(f"\n\t{nombre_1} NO esta en la lista")
if nombre_2 in lista:
    print(f"\n\t{nombre_2} esta en la lista")
else:
    print(f"\n\t{nombre_2} NO esta en la lista")


if __name__ == "__main__":
    print("You're on intro_03.py file")
