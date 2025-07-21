# *********************************************************
# CLASS 01 SECTION 02
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


# *********************************************************
# CLASS 01 EXERCISES 02
# *********************************************************



if __name__ == "__main__":
    print("You're on intro_02.py file")
