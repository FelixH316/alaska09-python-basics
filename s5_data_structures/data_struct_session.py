# *********************************************************
# COURSE 09 SESSION 05
# *********************************************************

"""
ESTRUCTURAS DE DATOS
Un conjunto de elementos es una colección de items, que son almacenados
    juntos de manera organizada. Algunos ejemplos de conjuntos de
    elementos en Python son las listas, los strings y los diccionarios.

LISTAS
Las listas pueden almacenar una colección de items en orden. Ellas son
    delimitadas por corchetes [] y sus elementos son separados por comas.

Estas pueden almacenar cualquier tipo de items, incluyendo números,
    strings, objetos, otras listas, entre otros. También nos permiten
    almacenar items de tipos de datos diferentes juntos en una única
    lista.
"""
lista = ["Pepe Camacho", 9.5, 9.0, 9.7, True]
type(lista)

"""
Las listas son organizadas en Python porque cada elemento de la lista
    tiene un índice que indica su posición al interior de la lista. Los
    índices comienzan en 0 van hasta el tamaño de la lista menos 1.

Tenemos entonces 5 elementos con índices que varían de 0 a 4,
    ordenadamente:

#             [0]           [1]   [2]   [3]    [4]
lista = ['Penélope Camacho', 9.5 , 9.0 , 9.7 , True]
En Python tenemos también los índices negativos que se inician en el
    último elemento con el valor de -1 y avanzan en el universo de los
    negativos hasta llegar al 1° elemento:

#             [-5]         [-4]  [-3]  [-2]   [-1]
lista = ['Penélope Camacho', 9.5 , 9.0 , 9.7 , True]
Logramos seleccionar separadamente cada elemento a través de sus
    respectivos índices. Colocando el nombre de la lista y en seguida
    el índice que será seleccionado.
"""
print(type(lista[0]))
print(type(lista[1]))
print(type(lista[-1]))

# Una forma más dinámica de trabajar item a item en una lista es utilizando un lazo for para leer un elemento a la vez.
for elemento in lista:
    print(elemento)

"""
SITUATION
    La nota 9.0 de Penélope necesita ser ajustada pues ganó 1 punto en
        su última nota por participación en clase. Entonces es
        necesario realizar un cambio en el índice 2 de 9.0 a 10.0
"""
lista[2] = 10.0
lista

# También podemos calcular el promedio del estudiante a partir de los datos que tenemos.
promedio = (lista[1] +  lista[2] + lista[3]) / 3
print(promedio)

""" STR SPLIT """
lenguaje = "Python"

# Sin embargo, es posible convertir una cadena en una lista mediante el
#   método split(). Este método divide la cadena en una lista de
#   cadenas, utilizando un delimitador especificado entre paréntesis.
#   Este delimitador debe ser una cadena. Como ejemplo, convirtamos la
#   cadena en una lista dividiéndola cada vez que aparezca el signo de
#   interrogación "?":

pregunta = "¿Quién vino primero? ¿El huevo? ¿O fue la serpiente?"
lista_palabras = pregunta.split('?')
print(lista_palabras)

# El delimitador no aparece en la separación. Si no se define un
#   delimitador, la cadena se separará por todos los espacios en blanco
#   en el texto
pregunta = "¿Quién vino primero? ¿El huevo? ¿O fue la serpiente?"
lista_palabras = pregunta.split()
print(lista_palabras)

# Lo contrario también es posible, ya que podemos convertir una lista
#   en una cadena mediante el método join(). Para usar esta función,
#   debemos definir el carácter que se utilizará para unir los
#   elementos de la lista y formar la cadena. Luego, usamos el método
#   join() pasando la lista como argumento. Veamos un ejemplo con una
#   lista que contiene el resultado de algunas mezclas de colores
#   primarios en pintura:
mezclas = ['Pinturas: rojo, azul y amarillo',
            'Verde: mezcla de azul y amarillo',
            'Naranja: mezcla de rojo y amarillo',
            'Morado: mezcla de rojo y azul']
unificador = '. '
cadena_mezclas = unificador.join(mezclas)
print(cadena_mezclas)


"""
MANIPULACIÓN DE LISTAS
Las listas son muy útiles en Python porque nos permiten almacenar y
    acceder a una colección de items de manera organizada y rápida.
    Estas también ofrecen muchos métodos útiles para manipular los
    items almacenados, como adicionar, remover, clasificar y buscar
    elementos.

Cantidad de elementos
    Usamos la función len() para descubrir la cantidad de elementos de
    un conjunto.
"""
print(len(lista))

"""
Partición
La partición de listas por indexación en Python es una técnica muy útil
    para seleccionar un subconjunto de elementos de una lista. Esta se
    realiza usando la sintaxis lista[inicio:fin], donde inicio es el
    índice del primer elemento que será incluído en la partición fin es
    el índice del primer elemento que será excluído de la partición.
"""
print(lista[0:2])
print(lista[:2])
print(lista[:3])
print(lista[:])

"""
append()
Añade un elemento al final de la lista.
"""
lista.append(promedio)
print(lista)

"""
extend()
Añade varios elementos al final de la lista

Añadiremos las notas [10.0,8.0,9.0] En la lista de Pepe Camacho
"""
lista.extend([10.0, 8.0, 9.0])
print(lista)

# A continuación te mostraremos lo que no puede realizarse con append
lista.append([10.0, 8.0, 9.0])
print(lista)

"""
remove()
Remueve un elemento específico de la lista
"""
lista.remove([10.0, 8.0, 9.0])
print(lista)


""" OTHER METHODS FOR LISTS"""
razas_de_perros = ['Labrador Retriever',
                   'Bulldog Francés',
                   'Pastor Alemán',
                   'Poodle']

# lista.insert(n, element)
# que permite insertar un elemento en una posición específica de la
#   lista. La sintaxis es lista.insert(indice, elemento), donde "lista"
#   es la lista que recibirá el nuevo elemento, "indice" es la posición
#   donde se insertará el nuevo elemento y "elemento" es el nuevo
#   elemento que se insertará
razas_de_perros.insert(1, 'Golden Retriever')
print(razas_de_perros)


# lista.pop(n)
# elimina el elemento en una posición específica de la lista y lo
#   devuelve como salida al ejecutar el método. Solo necesitamos
#   especificar, entre paréntesis, el índice del elemento que deseamos
#   eliminar, y se eliminará de la lista. Por lo tanto, eliminemos la
#   raza "Golden Retriever" que agregamos en el método anterior
print(razas_de_perros.pop(1))
print(razas_de_perros)

# lista.index()
# devuelve el índice de un elemento específico en la lista. Para
#   hacerlo, especificamos el elemento entre paréntesis. Para encontrar
#   el índice de la raza "Pastor Alemán" en la lista, hacemos lo
#   siguiente:
print(razas_de_perros.index('Pastor Alemán'))


# lista.sort()
# ordena los elementos de la lista en orden ascendente o descendente.
#   Si son palabras, el orden se basa en el orden alfabético o en el
#   orden inverso. Para ordenar los valores, simplemente llamamos al
#   método sort(), y la lista se organizará en orden. Para ordenar
#   alfabéticamente la lista de razas de perros, podemos usar el
#   siguiente código:
razas_de_perros.sort()
print(razas_de_perros)

"""
DICCIONARIOS
Los diccionarios son un tipo de estructura de datos que almacenan pares
    de llave-valor. Estos son delimitados por llaves {} y los pares
    llave-valor son separados por comas.

diccionario = {llave: valor}

La llave es un elemento único que identifica a un valor en el
    diccionario, mientras que el valor es el item que será almacenado
    para la llave. Las llaves y sus respectivos valores se pueden
    emplear para cualquier tipo de dato

Los diccionarios son útiles para almacenar y acceder a los datos de
    manera organizada y rápida. Se trata de un tipo de conjunto de
    elementos en Python, pues almacenan una colección de items
"""
diccionario = {
    "llave_1" : 1,
    "llave_2" : 2
}
    
print(diccionario)
print(type(diccionario))


"""
SITUATION

Vamos a crear un conjunto de datos con las informaciones de matrícula
    de un estudiante. Los datos son los siguientes:

matrícula: 2000168933
día de registro: 25
mes de registro: 10
grupo: 2E
"""
estudiante = {
    "matricula" : 2000168933,
    "dia_registro" : 25,
    "mes_registro" : 10,
    "grupo" : "2E"
}
print(estudiante)

print(estudiante["matricula"])
print(estudiante["grupo"])


# Es posible sustituir los valores dentro de una llave. Por ejemplo,
#   recibimos la información de que el grupo del estudiante que
#   registramos cambio a '2G' y ahora necesitamos cambiar el valor de
#   la llave 'grupo'

estudiante["grupo"] = "2G"
print(estudiante)


# También podemos añadir otros datos al diccionario. Vamos a añadir la
#   información sobre la modalidad de estudio, nuestro estudiante
#   estudiará inicialemente en la modalidad EAD
# Definiremos una llave llamada 'modalidad' con el valor 'EAD'
estudiante["modalidad"] = "EAD"
print(estudiante)

""" DICTIONARIES METHODS """
# pop()
#   Remueve un item de un diccionario y lo representa en la salida
print(estudiante.pop("grupo"))
print(estudiante)

# items()
#   Retorna una lista de pares llave-valor del diccionario
print(estudiante.items())
for par in estudiante.items():
    print(par)

# keys()
#   Retorna una lista de las llaves del diccionario
print(estudiante.keys())

# values()
#   Retorna una lista de los valores del diccionario.
print(estudiante.values())

# Lectura de valores con el lazo for
for llave in estudiante.keys():
    print(llave)

for llave, valor in estudiante.items():
    print(llave, " --> ", valor)


""" MORE ABOUT DICTIONARIES """

# Listas como valores de un elemento en un diccionario
tienda = {
    'nombres': ['televisión', 'celular', 'notebook', 'geladeira', 
                'estufa'],
    'precios': [2000, 1500, 3500, 4000, 1500]
}

for clave, elementos in tienda.items():
  print(f"Clave: {clave}\nElementos: ")
  for dato in elementos:
    print(dato)

# El primer bucle, el más externo, recorre los elementos dentro del
#   diccionario (claves y elementos). Sabiendo que los elementos son
#   listas, podemos acceder a los datos de las listas con otro bucle
#   anidado que se encuentra dentro del primer bucle. El bucle más
#   interno recorre los elementos de cada lista uno a uno e imprime los
#   valores dentro de ellas

# Además, podemos realizar operaciones comunes en las listas, como
#   agregar, eliminar o contar elementos en la lista asociada a una
#   clave del diccionario. Puedes copiar los códigos anteriores y
#   ejecutarlos en Colab para verificar la salida


"""
BUILT-IN FUNCTIONS
Durante las clases, trabajamos directamente con varias funciones
    incorporadas que son predefinidas y están disponibles por defecto
    en Python. Estas funciones trabajan como herramientas útiles para
    llevar a cabo tareas comunes, como conversiones de tipos,
    operaciones matemáticas, manipulación de cadenas y más, sin
    necesidad de escribir código adicional

Algunas de las funciones incorporadas que ya conocemos son: print(),
    input(), len(), int(), str(), float(), range(), chr(), etc. Pero
    hay otras además de estas que también son muy útiles, como: sum(),
    help() y dir(). ¿Las conocemos?
"""

# sum()
#   La función sum() permite sumar los elementos de una secuencia o
#   estructura de datos. En el siguiente ejemplo, vamos a sumar los
#   precios de productos:
precios = [100.0, 400.0, 200.0]
suma = sum(precios)
suma

# help()
#   La función help() se utiliza para acceder a la documentación de
#   funciones, métodos y otros elementos de Python. Muestra información
#   en inglés sobre la funcionalidad, sintaxis y uso de un objeto
#   específico. Para usar esta función, simplemente pasa el elemento
#   deseado entre paréntesis. Por ejemplo, vamos a verificar la
#   documentación de la función print():
print(help(print))

# dir()
# La función dir() se utiliza para mostrar una lista de atributos y
#   métodos asociados a un elemento. Por ejemplo, vamos a descubrir
#   todos los atributos y métodos de una lista:
lista = [1,2,3]
print(dir(lista))
