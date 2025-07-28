# *********************************************************
# COURSE 09 EXERCISES 05
# *********************************************************

"""
Vamos practicar el uso de estructuras de datos, como listas y
    diccionarios, a través de algunas actividades. Ahora que estamos
    avanzando en el contenido, podemos hacer los desafíos más
    interesantes. ¡Para ello, trabajaremos con proyectos de código!

Primero, resolveremos algunos problemas para calentar y prepararnos
    para los proyectos
"""

"""
    HW01 - ENTRENANDO LA PROGRAMACIÓN
"""

"""
01 - Crea un programa que tenga la siguiente lista con los gastos de
    una empresa de papel:

        [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

Con estos valores, crea un programa que calcule el promedio de gastos
Sugerencia: usa las funciones integradas sum() y len()
"""
lista_gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38,
                2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
print(len(lista_gastos))
promedio = sum(lista_gastos) / len(lista_gastos)
print(f"\n\tThe average spended was: {promedio}")


"""
02 - Con los mismos datos de la pregunta anterior, determina cuántas
    compras se realizaron por encima de 3000 reales y calcula el
    porcentaje con respecto al total de compras
"""
counter = 0
excessive = 0
for element in lista_gastos:
    if element > 3000:
        counter += 1
        excessive += element

total = (excessive * 100) / sum(lista_gastos)
print(f"\n\t{counter} purchases were made for more than 3k reais")
print(f"\tThe excessive purchases amount was {excessive} and it represents the {total:.2f}% from the total amount purchased")


"""
03 - Crea un código que solicite en una lista 5 números enteros
    aleatorios e imprima la lista
    
    Ejemplo: [1, 4, 7, 2, 4]
"""
# Lista que almacenará los 5 números enteros
lista_numeros = []

# Creamos un bucle que iterará 5 veces para recibir los 5 números
for i in range(0, 5):
    # Recopilamos el valor e lo insertamos en la lista 5 veces
    numero = int(input('Ingresa un número entero: '))
    lista_numeros.append(numero)

#Resultado
print(f'Lista de números ingresados: {lista_numeros}')


"""
04 - Recoge nuevamente 5 números enteros e imprime la lista en orden
    inverso al enviado
"""
# Lista que almacenará los 5 números enteros
lista_numeros = []

# Creamos un bucle que iterará 5 veces para recibir los 5 números
for i in range(0, 5):
    # Recopilamos el valor e lo insertamos en la lista 5 veces
    numero = int(input('Ingresa un número entero: '))
    lista_numeros.append(numero)

# Usamos la técnica de partición o slice para imprimir el resultado
# start : stop : step
print(f'Lista de números invertida: {lista_numeros[::-1]}')

"""
05 - Crea un programa que, al ingresar un número cualquiera, genere una
    lista que contenga todos los números primos entre 1 y el número
    ingresado
"""
# Recopilamos el número
numero = int(input("Ingresa un número entero: "))

# Lista para almacenar los números primos
lista_primos = []

# Bucle que recorre todos los números por debajo del número ingresado
for num in range(2, numero):
    # Primo es una bandera que nos permite saber si el valor analizado es
    # primo o no.
    primo = True

    # Probamos si todos los números por debajo del especificado en el
    # primer bucle pueden dar una división exacta
    for prueba_divisibles in range(2, num):
        if num % prueba_divisibles == 0:
            # Si es divisible por algún número, entendemos que el
            # número no es primo y terminamos el bucle interno con break
            primo = False
            break

    # La condición se convierte en el resultado booleano de primo: 
    # False. Ignoramos la condición True y ejecutamos el bloque del
    # if
    if primo:
        lista_primos.append(num)

# Resultado
print(f'Lista de números primos: {lista_primos}')


"""
06 - Escribe un programa que pida una fecha, especificando el día, mes
    y año, y determine si es válida para su análisis
"""
# Recopilamos la fecha
dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes: '))
año = int(input('Ingrese el año: '))

# Análisis de febrero
if mes == 2:
    # Verificamos si es o no un año bisiesto
    if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
        dias_febrero = 29
    else:
        dias_febrero = 28
    
    # Verificamos si el día ingresado coincide con el máximo de días de
    # febrero
    if dia >= 1 and dia <= dias_febrero:
        print('Fecha válida para Febrero')
    else:
        print('Fecha inválida para Febrero')

# Verificamos meses que terminan en 31 días
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia >= 1 and dia <= 31:
        print('Fecha válida para mes de 31 días')
    else:
        print('Fecha inválida para mes de 31 días')

# Verificamos meses que terminan en 30 días
elif mes in [4, 6, 9, 11]:
    if dia >= 1 and dia <= 30:
        print('Fecha válida para mes de 30 días')
    else:
        print('Fecha inválida para mes de 30 días')
# Si el mes no está entre 1 y 12
else:
    print('Fecha inválida para el mes ingresado')


"""
    HW02 - MOMENTO DE PROYECTOS
"""

"""
07 - Para un estudio sobre la multiplicación de bacterias en una
    colonia, se recopiló el número de bacterias multiplicadas por día y
    se puede observar a continuación: 
        
        [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
    
    Con estos valores, crea un código que genere una lista que contenga
        el porcentaje de crecimiento de bacterias por día, comparando
        el número de bacterias en cada día con el número de bacterias
        del día anterior
    
    Sugerencia: para calcular el porcentaje de crecimiento, utiliza la
        siguiente ecuación:
            100 * (muestra_actual - muestra_anterior) / muestra_anterior
"""
# Lista de crecimiento de bacterias
bacterias_colonia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

# Lista que almacenará las tasas de crecimiento
porcentaje_crecimiento = []

# Recorremos los índices de 1 a 9 para comparar los valores actuales
# con los anteriores
for i in range(1, len(bacterias_colonia)):
    # Realizamos el cálculo: 100 * (muestra_actual - muestra_anterior) / (muestra_anterior)
    porcentaje = 100 * (bacterias_colonia[i] - bacterias_colonia[i-1]) / (bacterias_colonia[i-1])
    
    # Agregamos el resultado a la lista porcentaje_crecimiento
    porcentaje_crecimiento.append(porcentaje)

# Resultado
print(f'Porcentajes de crecimiento:\n{porcentaje_crecimiento}')


"""
08 - Para una selección de productos alimenticios, debemos separar el
    conjunto de IDs proporcionados por números enteros, sabiendo que
    los productos con ID par son dulces y los que tienen ID impar son
    amargos. Crea un código que recoja 10 IDs. Luego, calcula y muestra
    la cantidad de productos dulces y amargos
"""
# Lista que contendrá los valores de IDs
ids = []
# Variables contadoras de dulces y amargos
dulce = 0
amargo = 0

# Creamos un bucle que iterará 10 veces para recopilar los 10 IDs
for i in range(0,10):
    # Recopilamos el ID y lo agregamos a la lista
    ids.append(int(input(f'Ingrese el ID {i+1}°: ')))

# Leemos todos los elementos de la lista de IDs y los asignamos a id
for id in ids:
    # Verificamos si los elementos son pares o impares para llevar el conteo
    if id % 2 == 0:
        dulce += 1
    else:
        amargo += 1

# Resultado
print(f'Cantidad de productos dulces: {dulce}')
print(f'Cantidad de productos amargos: {amargo}')


"""
09 - Desarrolla un programa que informe la puntuación de un estudiante
    de acuerdo con sus respuestas. Debe pedir la respuesta del
    estudiante para cada pregunta y verificar si la respuesta coincide
    con el resultado. Cada pregunta vale un punto y hay opciones: A, B,
    C o D

    Resultado del examen:
    01 - D
    02 - A
    03 - C
    04 - B
    05 - A
    06 - D
    07 - C
    08 - C
    09 - A
    10 - B
"""
# Inicializamos los datos
respuestas = []  # Lista para almacenar las respuestas

# Lista de respuestas correctas
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
nota = 0  # Acumulará la nota total

# Recopilamos las respuestas del estudiante
for i in range(0, 10):
    respuestas.append(input(f'Introduzca la respuesta a la pregunta {i + 1}: ').upper())

# Verificamos si las respuestas coinciden y las sumamos a la nota
for i in range(0, 10):
    if respuestas[i] == gabarito[i]:
        nota += 1

# Mostrando la nota final
print(f'Nota final: {nota}')


"""
10 - Un instituto de meteorología desea realizar un estudio de la
    temperatura media de cada mes del año. Para ello, debes crear un
    código que recoja y almacene esas temperaturas medias en una lista. 
    
    Luego, calcula el promedio anual de las temperaturas y muestra
        todas las temperaturas por encima del promedio anual y en qué
        mes ocurrieron, mostrando los meses por su nombre (Enero,
        Febrero, etc.)
"""
# Recopilamos la lista de temperaturas mensuales
temperaturas_mensuales = []

for i in range(0, 12):
    temperaturas_mensuales.append(float(input(f'Ingrese la temperatura promedio del mes {i+1}: ')))

# Creamos una lista auxiliar para los nombres de los meses
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Calculamos el promedio
media_anual = sum(temperaturas_mensuales) / len(temperaturas_mensuales)

# Resultado
print("Temperaturas por encima del promedio en: ")
for i in range(0, 12):
    # Verificamos todas las temperaturas en comparación con la media anual
    if temperaturas_mensuales[i] > media_anual:
        # Dado que los índices de los meses corresponden a las
        # temperaturas, podemos imprimirlos con el mismo índice
        print(meses[i])


"""
11 - Una empresa de comercio electrónico está interesada en analizar
    las ventas de sus productos. Los datos de ventas se han almacenado
    en un diccionario:

    {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

Escribe un código que calcule el total de ventas y el producto más
    vendido
"""
products = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60,
            'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

total = 0
star_quantity = 0
star_product = None

for key in products.keys():
    total += products[key]
    if products[key] > star_quantity:
        star_quantity = products[key]
        star_product = key
print(f"\n\tTotal sells amount was: {total} and the star product was: {star_product}")


"""
12 - Se realizó una encuesta de mercado para decidir cuál diseño de
    marca infantil es más atractivo para los niños. Los votos de la 
    encuesta se pueden ver a continuación:

    Tabla de votos de la marca
    Diseño 1 - 1334 votos
    Diseño 2 - 982 votos
    Diseño 3 - 1751 votos
    Diseño 4 - 210 votos
    Diseño 5 - 1811 votos

Adapta los datos proporcionados a una estructura de diccionario. A
    partir de ello, informa el diseño ganador y el porcentaje de votos
    recibidos.
"""
designs = {"design1" : 1334, "design2" : 982, "design3" : 1751,
           "design4" : 210, "design5" : 1811}

most_votes = 0
winner = None
total_votes = 0

for key, value in designs.items():
    total_votes += value
    if value > most_votes:
        most_votes = value
        winner = key
print(f"\n\tThe winner is {winner} with the {(most_votes * 100) / total_votes : .2f}% of the votes")


"""
13 - Los empleados de un departamento de tu empresa recibirán una
    bonificación del 10% de su salario debido a un excelente
    rendimiento del equipo. El departamento de finanzas ha solicitado
    tu ayuda para verificar las consecuencias financieras de esta
    bonificación en los recursos. Se te ha enviado una lista con los 
    salarios que recibirán la bonificación: 
    
        [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
    
    La bonificación de cada empleado no puede ser inferior a 200. En el
        código, convierte cada uno de los salarios en claves de un
        diccionario y la bonificación de cada salario en el valor 
        correspondiente.
    
    Luego, informa el gasto total en bonificaciones, cuántos empleados
        recibieron la bonificación mínima y cuál fue el valor más alto
        de la bonificación proporcionada.
"""
salaries = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
bonus = {}
abonos_minimos = 0

for i, money in enumerate(salaries):
    label = "empleado" + str(i)
    if money * 0.10 > 200:
        bonus[label] = money * 0.10
    else:
        abonos_minimos += 1
        bonus[label] = 200

bonus_total = 0
greatest_bonus = 0
people = None
for key, value in bonus.items():
    bonus_total += value
    if value > greatest_bonus:
        greatest_bonus = value
        people = key
    print(f"\tThe employee: {key} has a bonus of: {value:.2f}")

print(f"\tThe bonus total amount was: {bonus_total:.2f}")
print(f"\tThe greatest bonus was: {greatest_bonus:.2f} for {people}")
print(f"\tThere were {abonos_minimos} minimum bonuses given")


"""
14 - Un equipo de científicos de datos está estudiando la diversidad
    biológica en un bosque. El equipo recopiló información sobre el
    número de especies de plantas y animales en cada área del bosque y
    almacenó estos datos en un diccionario. En él, la clave describe el
    área de los datos y los valores en las listas corresponden a las
    especies de plantas y animales en esas áreas, respectivamente

    {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

Escribe un código para calcular el promedio de especies por área e
    identificar el área con la mayor diversidad biológica. 

Sugerencia: utiliza las funciones incorporadas sum() y len()
"""
species = {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492],
           'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688],
           'Área Centro': [22558, 45148]}

greatest_area = None
greatest_number = 0
general_average = 0
for key, lista in species.items():
    total_area_species = sum(lista)
    area_average = total_area_species / len(lista)
    if total_area_species > greatest_number:
        greatest_area = key
    general_average += area_average
    print(f"\t{key} species average: {area_average}")
general_average /= len(species)
print(f"\tThe area with the most biological diversity is: {greatest_area}")
print(f"\tThe general average is: {general_average:.2f}")

"""
15 - El departamento de Recursos Humanos de tu empresa te pidió ayuda
    para analizar las edades de los colaboradores de 4 sectores de la
    empresa. Para ello, te proporcionaron los siguientes datos:

    {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Dado que cada sector tiene 10 colaboradores, construye un código que
    calcule la media de edad de cada sector, la edad media general
    entre todos los sectores y cuántas personas están por encima de la
    edad media general
"""
sectors = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
             'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
             'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
             'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

general_avg = 0
over_avg_counter = 0
for sector, lista_edades in sectors.items():
    sector_avg = sum(lista_edades)
    sector_avg /= len(lista_edades)
    print(f"\t{sector} average: {sector_avg}")
    general_avg += sector_avg

general_avg /= len(sectors)

for lista_edades in sectors.values():
    for edad in lista_edades:
            if edad > general_avg:
                over_avg_counter += 1
print(f"\tGeneral average: {general_avg}")
print(f"\tEmployees over average: {over_avg_counter}")
