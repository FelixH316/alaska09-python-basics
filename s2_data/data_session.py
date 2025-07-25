# *********************************************************
# COURSE 09 SESSION 02
# *********************************************************

# Si es el mismo dato utiliza el mismo espacio de memoria
edad = 5
print(id(edad))

numerocinco = 5
print(id(numerocinco))

# Tipos de datos
type(edad)

promedio = 9.5
type(promedio)

nombre = "Felix"
type(nombre)

v = True
type(v)

# En un conjunto de datos escolares podemos tener varios tipos de datos
#   Supongamos que tenemos acceso a la ficha de datos del alumno 
#   Penélope Camacho, cómo transformamos este nombre en variables de
#   de Python?
# Ficha:
#   Nombre: Penélope Camacho
#   Edad: 11 años
#   Promedio del semestre: 9.75
#   Situación de aprobación: Verdadera (aprobada)
nombre_estudiante = "Penélope Camacho"
edad_estudiante = 11
promedio_estudiante = 9.75
aprobado = True

print(nombre_estudiante, edad_estudiante, promedio_estudiante, aprobado)
print(type(nombre_estudiante), type(edad_estudiante), type(promedio_estudiante), type(aprobado))

"""
VARIABLES NUMÉRICAS

SITUATION 01
Entre los tipos de datos numéricos vamos a enfocarnos en los tipos int
    float.

Tenemos una tabla de información sobre los diversos cargos, cantidad de
    personas empleadas y el salario correspondiente:

    Cargo       | Cantidad | Salario
    Vigilante   | 5        | 300
    Docente     | 16       | 500
    Coordinador | 2        | 600

Necesitamos trabajar con estos datos para obtener:
    + La cantidad de empleados
    + La diferencia entre el salario más bajo y más alto
    + El promedio ponderado de los salarios de los empleados de la
        escuela
"""
c_vigilante = 5
s_vigilante = 300

c_docente = 16
s_docente = 500

c_coordinador = 2
s_coordinador = 600

total_empleados = c_vigilante + c_docente + c_coordinador
print(f"Total employees: {total_empleados}")

diferencia = s_coordinador - s_vigilante
print(f"Difference between coordinator and security salary: {diferencia}")

promedio_salarios = (c_vigilante * s_vigilante 
                     + c_docente * s_docente 
                     + c_coordinador * s_coordinador) / total_empleados
print(f"Average salary: {promedio_salarios}")
print(type(promedio_salarios))


"""
STRINGS
Strings hace referencia a un conjunto de caracteres formando un texto.

Podemos crear Strings cuando atribuimos un dato a una variable entre
    comillas sencillas (') o comillas dobles (").

Las variables textuales son objetos que poseen métodos que nos ayudan a
    formatear strings. Los métodos los podemos ejecutar al definir un 
    objeto de acuerdo con la siguiente estructura:

    objeto.metodo()

    Existen métodos que no necesitan los (), siempre es una buena
        práctica verificar la documentación para cada caso.
"""
t = "Alura"
print(type(t))

""" 
SITUATION 02
Recibimos una variable con el nombre de una profesora de la escuela 
    para añadirla a los registros. Sin embargo, necesitamos darle un
    tratamiento a este texto antes de insertarlo al sistema.

    El objetivo final es que el nombre aparezca de la siguiente forma:
        'MICAELA DE LOS SANTOS'
    
    Observaciones:
    1° Los métodos devuelven una tranformación, no son ejecutados
        directamente sobre la variable donde está almacenado el texto.

    2° Adicionalmente, podemos acumular la ejecución de los métodos.
"""
texto = "  Micaela de los Sanyos  "

id(texto)
print(texto.upper())
print(texto.lower())
print(texto.strip())
print(texto.replace('y', 't'))
print(texto)

# Para que la transformación se pueda ejecutar debemos atribuir la 
#   salida de las transformaciones a las variables.
print("\nvar: nuevo_texto")
nuevo_texto = texto.strip().replace('y', 't').upper()
print(nuevo_texto)
print(id(texto), id(nuevo_texto))

print("\nvar: texto")
texto = texto.strip().replace('y', 't').upper()
print(texto)
print(id(texto), id(nuevo_texto))
print('\n')

# Existen otro operadores como exponenciación **
num = 2 ** 3 # num = 2^3
print(num)

# Módulo de una división
num = 7 % 3 # num = modulo de (7 / 3)
print(num)

# División entera
num = 7 // 3 # num = numero entero de la división (7 / 3)
print(num)

"""
CAPTURANDO DATOS
En algunas aplicaciones necesitamos capturar los valores del usuario de
    nuestro proyecto. En python, logramos capturar los datos del 
    usuario a través del comando input().

Para ejecutar la captura debemos atribuir el resultado de esta función 
    a una variable.
"""
nombre = input("Escribe tu nombre: ")
print(type(nombre))

"""
La salida de este comando siempre será una string. Esto quiere decir
    que aunque capturemos un valor de variable numérica, este será de 
    tipo string.

Entonces, será necesario convertir el resultado cuando no se desea 
    utilizar el valor como tipo string.

Existen funciones para la conversión de valores:
    + Enteros: int(dato_para_conversion)
    + Coma flotante: float(dato_para_conversion)
    + String: str(dato_para_conversion)
    + Booleano: bool(dato_para_conversion)
"""
year_in = input("Digita el año de admisión: ")
print(year_in)
print(type(year_in))

year_out = input("Digita el año de admisión: ")
print(year_out)
print(type(year_out))

# Error porque son str ambos
# print(year_out - year_in)

year_in = int(year_in)
year_out = int(year_out)
print(year_out - year_in)

admition_grade = float(input("Digita la nota de admisión: "))
print(admition_grade)
print(type(admition_grade))


# Trataremos de representar mejor ahora el resultado de la 
#   transformaciónque obtuvimos. Nosotros podemos formatear y presentar
#   nuestro resultado mezclando strings con valores no textuales. Para
#   ello utilizamos la estructura de formatación f con strings.
print(f"\tEl año de admisión fue {year_in} \n\tLa nota de admisión fue: {admition_grade}")


""" ELEMENTOS UNICODE """
print(chr(64))

# Hello world from Unicode
print(chr(72) + chr(111) +  chr(108) + chr(97))


""" 
OTROS FORMATOS DE print()
Operador de formateo %

data_type | key_word
str       | %s
int       | %d
float     | %f
char      | %c
"""
nombre_alumno = 'Penélope Camacho'
print('Nombre del alumno: %s' %(nombre_alumno))

# Multiple var for % operator
nombre_alumno = 'Penélope Camacho'
edad_alumno = 11
media_alumno = 9.95
print('Nombre del alumno es %s, tiene %d años y su media es %f.' %(nombre_alumno, edad_alumno, media_alumno))

# Using % operator with float 
print('Nombre del alumno es %s, tiene %d años y su media es %.2f.' %(nombre_alumno, edad_alumno, media_alumno))

# Using % operator with Bool
x = True
print("Valor de x: %s" % str(x))


""" 
OTROS FORMATOS DE print()
.format()
"""
nombre_alumno = 'Penélope Camacho'
print('Nombre del alumno: {}'.format(nombre_alumno))

# Using .format() with multiple vars
nombre_alumno = 'Fabricio Daniel'
edad_alumno = 15
media_alumno = 9.95
print('Nombre del alumno es {}, tiene {} años y su media es {}.' .format(nombre_alumno, edad_alumno, media_alumno))


""" CARACTERES ESPECIALES """
# Salto de línea
print("Estudiar es un esfuerzo constante,\nEs como cultivar una planta,\nNecesitamos dedicación y paciencia,\nPara ver madurar el fruto.")

# Tabulación
print('Cantidad\tCalidad\n5 muestras\tAlta\n3 muestras\tBaja')

# Barra invertida
print("Ruta del archivo: C:\\archivos\\documento.csv")

# Escape para comillas dobles
print("Una vez oí: \"Los frutos del conocimiento son los más dulces y duraderos de todos.\"")

# Escape para comillas simples
print('Mi profesora una vez dijo: \'Estudiar es la clave del éxito.\'')


if __name__ == "__main__":
    print("You're on intro_02.py file")
