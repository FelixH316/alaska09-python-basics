# *********************************************************
# CLASS 01 EXERCISES 03
# *********************************************************
"""
Vamos practicar el uso de estructuras condicionales como el if, else y
    elif a través de algunas actividades. Ahora que estamos avanzando 
    en los contenidos, podemos hacer los desafíos más interesantes: 
    ¡trabajaremos en proyectos de código! Resuelve los problemas
    iniciales para prepararte para los proyectos
"""

# HW 01 - ENTRENANDO LA PROGRAMACIÓN
"""
01 - Escribe un programa que pida a la persona usuaria que proporcione
    dos números y muestre el número más grande
"""
num1 = float(input("Input a number: "))
num2 = float(input("Input another number: "))
if num1 == num2:
    print(f"Your numbers inputed were {num1} and {num2}, they are equal")
elif num1 > num2:
    print(f"Your numbers inputed were {num1} and {num2}, the greatest is: {num1}")
else:
    print(f"Your numbers inputed were {num1} and {num2}, the greatest is: {num2}")

"""
02 - Escribe un programa que solicite el porcentaje de crecimiento de
    producción de una empresa e informe si hubo un crecimiento
    (porcentaje positivo) o una disminución (porcentaje negativo).
"""
num1 = float(input("Input the percentage growth in the company's production: "))
if num1 == 0:
    print("We stayed the same")
elif num1 > 0:
    print(f"There was growth of {num1}%")
else:
    print(f"There was a decrease of {num1 * -1}%")


"""
03 - Escribe un programa que determine si una letra proporcionada por
    la persona usuaria es una vocal o una consonante.
"""
vowels = "a e i o u"
char = input("Input any letter: ").lower()
if char in vowels:
    print(f"The letter {char} is a vowel")
else:
    print(f"The letter {char} is a consonant")


"""
04 - Escribe un programa que lea valores promedio de precios de un
    modelo de automóvil durante 3 años consecutivos y muestre el valor
    más alto y más bajo entre esos tres años.
"""
avg_car_value_yearly = [120000, 90000, 30000, 450000]
greatest = avg_car_value_yearly[0]
lowest = avg_car_value_yearly[0]
for i, value in enumerate(avg_car_value_yearly):
    print(f"i value {i}")
    if (i+1) == len(avg_car_value_yearly):
        pass
    else:
        if avg_car_value_yearly[i+1] > value:
            greatest = avg_car_value_yearly[i+1]
        if avg_car_value_yearly[i+1] < value:
            lowest = avg_car_value_yearly[i+1]
print(f"\tThe greatest value was {greatest} and the lowest was {lowest}")


"""
05 - Escribe un programa que pregunte sobre el precio de tres productos
    e indique cuál es el producto más barato para comprar.
"""
# Same


"""
06 - Escribe un programa que lea tres números y los muestre en orden
    descendente.
"""
import random
rand_list = []
for value in range(3):
    value = random.randint(0, 100)
    rand_list.append(value)
print(f"\tThe list is: {rand_list}")
for j in range(len(rand_list)):
    for i, value in enumerate(rand_list):
        if (i+1) == len(rand_list):
            pass
        else:
            if rand_list[i+1] > value:
                aux = value
                rand_list[i] = rand_list[i+1]
                rand_list[i+1] = aux
print(f"\tThe final list is: {rand_list}")


"""
07 -Escribe un programa que pregunte en qué turno estudia la persona
    usuaria ("mañana", "tarde" o "noche") y muestre el mensaje
    "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o 
    "Valor Inválido!", según el caso.
"""
sp = "mañana tarde noche"
shift = input("Write the shift you take \"morning\", \"afternoon\" or \"night\": ")
if shift == "morning":
    print("\tGood Morning!")
elif shift == "afternoon":
    print("\tGood Afternoon!")
elif shift == "night":
    print("\tGood Night!")
elif shift in sp:
    print("\tSorry I don't speak spanish")
else:
    print("\tI couldn't uderstand you U_u")

"""
08 - Escribe un programa que solicite un número entero a la persona
    usuaria y determine si es par o impar. Pista: Puedes usar el
    operador módulo (%).
"""
value = random.randint(0, 999999)
if value % 2 == 0:
    print(f"\n\tYour value is {value} and it's even")
else:
    print(f"\n\tYour value is {value} and it's odd")

"""
09 - Escribe un programa que pida un número a la persona usuaria y le
    informe si es entero o decimal.
"""
# For strings
value = input("Input any number: ")
if "." in value:
    print(f"\n\tYour value is {value} and it's decimal")
else:
    print(f"\n\tYour value is {value} and it's integer")

# For numbers
value = float(value)
if value % 1 == 0:
    print(f"\n\tYour value is {value} and it's integer")
else:
    print(f"\n\tYour value is {value} and it's decimal")


# HW 02 - MOMENTO DE PROYECTOS
"""
10 - Un programa debe ser escrito para leer dos números y luego
    preguntar a la persona usuaria qué operación desea realizar. El
    resultado de la operación debe incluir información sobre el número,
    si es par o impar, positivo o negativo, e entero o decimal.
"""
num1 = float(input("Input a number: "))
num2 = float(input("Input another number: "))
# TODO


"""
11 - Escribe un programa que pida a la persona usuaria tres números que
    representan los lados de un triángulo. El programa debe informar si
    los valores pueden utilizarse para formar un triángulo y, en caso 
    afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta
    algunas sugerencias:

    + Tres lados forman un triángulo cuando la suma de cualesquiera dos
        lados es mayor que el tercero

    + Triángulo Equilátero: tres lados iguales

    + Triángulo Isósceles: dos lados iguales

    + Triángulo Escaleno: tres lados diferentes
"""
side1 = float(input("\nInput triangle side 1: "))
side2 = float(input("Input triangle side 2: "))
side3 = float(input("Input triangle side 3: "))
if (side1 + side2) > side3:
    print("\tYou have a triangle")
    if side1 == side2 and side2 == side3:
        print("\tYour triangle is equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("\tYour triangle is isosceles")
    else:
        print("\tYour triangle is scalene")
else:
    print("\tYou have a handful of twigs")


"""
12 - Un establecimiento está vendiendo combustibles con descuentos
    variables. Para el etanol, si la cantidad comprada es de hasta 15
    litros, el descuento será del 2% por litro. En caso contrario, será
    del 4% por litro. Para el diésel, si la cantidad comprada es de
    hasta 15 litros, el descuento será del 3% por litro. En caso
    contrario, será del 5% por litro. El precio por litro de diésel es
    de R$ 2,00 y el precio por litro de etanol es de R$ 1,70. Escribe 
    un programa que lea la cantidad de litros vendidos y el tipo de
    combustible (E para etanol y D para diésel) y calcule el valor a
    pagar por el cliente. Ten en cuenta algunas sugerencias:

    + El valor del descuento será el producto del precio por litro, la
        cantidad de litros y el valor del descuento.

    + El valor a pagar por un cliente será el resultado de la
        multiplicación del precio por litro por la cantidad de litros
        menos el valor del descuento resultante del cálculo.
"""
# TODO


"""
13 - En una empresa de venta de bienes raíces, debes crear un código
    que analice los datos de ventas anuales para ayudar a la dirección
    en la toma de decisiones. El código debe recopilar los datos de
    cantidad de ventas durante los años 2022 y 2023 y calcular la
    variación porcentual. A partir del valor de la variación, se deben
    proporcionar las siguientes sugerencias:

    + Para una variación superior al 20%: bonificación para el equipo
        de ventas.

    + Para una variación entre el 2% y el 20%: pequeña bonificación
        para el equipo de ventas.

    + Para una variación entre el 2% y el -10%: planificación de
        políticas de incentivo a las ventas.

    + Para bonificaciones inferiores al -10%: recorte de gastos.
"""
percent_2022 = random.random() * 100
percent_2023 = random.random() * 100

print(f"\n\tPercentage 2022: [{percent_2022:.2f}]")
print(f"\tPercentage 2023: [{percent_2023:.2f}]")
difference = percent_2023 - percent_2022
print(f"\tPercentage variation: [{difference:.2f}]")
if difference > 20.00:
    print("\tBonus for the sales team")
elif difference > 2.00 and difference < 20.00:
    print("\tSmall bonus for the sales team")
elif difference > -10.00 and difference < 2.00:
    print("\tPlanning sells incentive policies")
elif difference < -10.00:
    print("\tSpending cuts")
else:
    print("\tINVALID VALUES")
