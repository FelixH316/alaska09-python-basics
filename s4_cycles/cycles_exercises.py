# *********************************************************
# COURSE 09 EXERCISES 04
# *********************************************************

"""
Vamos practicar el uso de estructuras de repetición como el "while" y
    el "for" a partir de algunas actividades. Ahora que estamos
    avanzando en el contenido, podemos hacer los desafíos más
    interesantes. ¡Para ello, trabajaremos en proyectos de código!

Comencemos resolviendo algunos problemas para calentar y prepararnos
    para los proyectos
"""

# HW 01 - ENTRENANDO LA PROGRAMACIÓN

"""
01 - Escribe un programa que solicite dos números enteros e imprima
    todos los números enteros entre ellos.
"""
# TODO Code Review
# Recolectamos los valores de inicio y fin
inicio = int(input('Ingresa el primer número entero: '))
fin = int(input('Ingresa el segundo número entero: '))

# Verificamos si el valor de inicio es menor que el fin
if inicio < fin:
    # Podemos imprimir los enteros entre el valor menor y el valor mayor
    for i in range(inicio + 1, fin): 
        print(i)
elif inicio > fin:
    for i in range(fin + 1, inicio):
        print(i)
else: # En caso de que los números sean iguales, no podemos imprimir ninguna secuencia.
    print('Los números son iguales.')

"""
02 - Escribe un programa para calcular cuántos días tomará que la
    colonia de una bacteria A supere o iguale a la colonia de una
    bacteria B, basado en tasas de crecimiento del 3% y 1.5%,
    respectivamente. Supón que la colonia A comienza con 4 elementos y
    B con 10.
"""
a = 4
rate_a = 1.03
b = 10
rate_b = 1.015
days = 0
while a < b:
    a *= rate_a
    b *= rate_b
    days += 1
if a == b:
    print(f"\tThe bacteria colony A will equal colony B in {days} days")
elif a > b:
    print(f"\tThe bacteria colony A will overcome colony B in {days} days")

"""
03 - Para procesar una cantidad de 15 datos de evaluaciones de usuarios
    de un servicio de la empresa, necesitamos verificar si las
    calificaciones son válidas. Por lo tanto, escribe un programa que
    recibirá calificaciones del 0 al 5 y verificará si son valores
    válidos. Si se ingresa una calificación superior a 5 o inferior a
    0, se repetirá hasta que el usuario ingrese un valor válido.
"""
# Bucle para recopilar las 15 notas
for i in range(15):
    nota = float(input(f"Ingresa la nota del usuario {i}: "))
    # Verifica si la nota está entre 0 y 5
    # Si no lo está, el bucle se repetirá hasta que se obtenga un valor válido
    while (nota < 0) or (nota > 5):
        nota = float(input(f"Nota no válida, ingresa nuevamente la nota del usuario {i}: "))

print('Verificación completa. Todas las notas son válidas.')

"""
04 - Desarrolla un programa que lea un conjunto indefinido de
    temperaturas en grados Celsius y calcule su promedio. La lectura
    debe detenerse al ingresar el valor -273°C.
"""
# TODO: Code Review
# Recopilamos la temperatura
temperatura = float(input('Ingresa la temperatura en grados Celsius: '))

# Inicializamos un contador y una suma para calcular el promedio
contador = 0
suma = 0

# Nuestro código se ejecuta hasta que el valor de temperatura sea igual a -273
while temperatura != -273:
    # La suma se actualiza sumando la temperatura a la variable suma
    suma += temperatura
    # Contamos la cantidad de valores recopilados con el contador
    contador += 1
    # Recopilamos nuevamente la temperatura
    temperatura = float(input('Ingresa la temperatura en grados Celsius: '))

promedio = suma / contador

print(f'El promedio de las temperaturas es: {promedio}')

"""
05 - Escribe un programa que calcule el factorial de un número entero
    proporcionado por el usuario. Recuerda que el factorial de un
    número entero es el producto de ese número por todos sus
    antecesores hasta llegar al número 1. Por ejemplo, el factorial de
    5 es 5 x 4 x 3 x 2 x 1 = 120
"""
value = int(input("\nEnter a integer number: "))
result = value
counter = value
while counter > 1:
    counter -= 1
    result *= counter
print(f"\tThe factorial of {value} is: {result}")

# HW 02 - MOMENTO DE LOS PROYECTOS
"""
06 - Escribe un programa que genere la tabla de multiplicar de un
    número entero del 1 al 10, según la elección del usuario. Como
    ejemplo, para el número 2, la tabla de multiplicar debe mostrarse
    en el siguiente formato:

Tabla de multiplicar del 2:
    2 x 1 = 2
    2 x 2 = 4
    [...]
    2 x 10 = 20
"""
# Solicita el número
num = int(input("Ingresa un número entero del 1 al 10: "))

# Generamos la tabla de multiplicar
print(f'Tabla de multiplicar del {num}:')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

"""
07 - Los números primos tienen diversas aplicaciones en Ciencia de
    Datos, como en criptografía y seguridad. Un número primo es aquel
    que es divisible solo por sí mismo y por 1. Por lo tanto, crea un
    programa que solicite un número entero y determine si es un número
    primo o no.
"""
# Recopilamos el número
num = int(input('Ingresa un número entero: '))

# Los números enteros iguales o menores que 1 no se consideran primos
if num > 1:
    for i in range(2, num):
        # Verificamos todos los residuos de la división entre todos los
        #   números menores que num
        # Si algún residuo es 0, significa que es divisible por otro
        #   número además de sí mismo y 1
        if (num % i) == 0:
            print(f'{num} no es un número primo')
            break
    else:
        print(f'{num} es un número primo')
else:
    print(f'{num} no es un número primo')

"""
08 - Vamos a comprender la distribución de edades de los pensionistas
    de una empresa de seguros. Escribe un programa que lea las edades
    de una cantidad no informada de clientes y muestre la distribución
    en los intervalos [0-25], [26-50], [51-75] y [76-100]. La entrada
    de datos se detendrá al ingresar un número negativo
"""
# Recopilamos las edades de los clientes
edad = int(input("Input the age (or a negative number to finish): "))

# Inicializamos las variables de conteo
contador_0_25 = 0 # contador de edades entre 0 y 25
contador_26_50 = 0 # contador de edades entre 26 y 50
contador_51_75 = 0 # contador de edades entre 51 y 75
contador_76_100 = 0 # contador de edades entre 76 y 100

# Nuestro código se ejecuta hasta que el valor de edad sea negativo
while edad >= 0:
    # Contamos cada caso
    if edad >= 0 and edad <= 25:
        contador_0_25 += 1
    elif edad >= 26 and edad <= 50:
        contador_26_50 += 1
    elif edad >= 51 and edad <= 75:
        contador_51_75 += 1
    elif edad >= 76 and edad <= 100:
        contador_76_100 += 1
    
    # Repetimos el proceso de entrada de datos hasta que se ingrese un número negativo    
    edad = int(input('Ingresa la edad (o un número negativo para finalizar): '))

# Mostramos los resultados
print('Distribución de edades:')
print('[0-25]:', contador_0_25)
print('[26-50]:', contador_26_50)
print('[51-75]:', contador_51_75)
print('[76-100]:', contador_76_100)

"""
09 - En una elección para la gerencia de una empresa con 20 empleados,
    hay cuatro candidatos. Escribe un programa que calcule al ganador
    de la elección. La votación se realizó de la siguiente manera:

    Cada empleado votó por uno de los cuatro candidatos (representados
        por los números 1, 2, 3 y 4).

    También se contaron los votos nulos (representados por el número 5)
        y los votos en blanco (representados por el número 6).

    Al final de la votación, el programa debe mostrar el número total
        de votos para cada candidato, los votos nulos y los votos en 
        blanco. Además, debe calcular y mostrar el porcentaje de votos
        nulos con respecto al total de votos y el porcentaje de votos
        en blanco con respecto al total de votos.
"""
# TODO: Code Review
# Inicializamos las variables contadoras
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_blanco = 0

# Inicio del bucle para leer los votos
for i in range(0, 20):
    voto = int(input("Ingresa tu voto: "))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_blanco += 1
    else:
        print("Voto inválido.")

print(f"Votos candidato 1: {votos_candidato1}")
print(f"Votos candidato 2: {votos_candidato2}")
print(f"Votos candidato 3: {votos_candidato3}")
print(f"Votos candidato 4: {votos_candidato4}")
print(f"Votos nulos: {votos_nulos}")
print(f"Votos en blanco: {votos_blanco}")
print(f"Porcentaje de votos nulos: {(votos_nulos / 20 * 100)}")
print(f"Porcentaje de votos en blanco: {(votos_blanco / 20 * 100)}")
