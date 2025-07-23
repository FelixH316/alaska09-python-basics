# *********************************************************
# CLASS 01 EXERCISES 02
# *********************************************************
# HW 01 - Recopilación y muestra de datos
print("RECOPILACIÓN Y MUESTRA DE DATOS")
name = input("Ingresa tu nombre: ")

age = input("Ingresa tu edad: ")

height = input("Ingresa tu altura en metros: ")
print(f"\tHola {name}, tienes {age} años y mides {height} m")


# HW 02 - Calculadora de operadores
print("\n\nCALCULADORA DE OPERADORES")
# 04
val1 = float(input("Ingresa un número: "))
val2 = float(input("Ingresa otro número: "))
print(f"\tTus números son: {val1} y {val2}")
print(f"\tLa suma es: {val1 + val2}")

# 05
val3 = float(input("\nIngresa un tercer número: "))
print(f"\tLa suma de los tres es: {val1 + val2 + val3}")

# 06
print(f"\n\tLa resta de {val1} menos {val2} es: {val1 - val2}")

# 07
print(f"\n\tLa multiplicación de {val1} por {val2} es: {val1 * val2}")

# 08
if val2 <= 0:
    print(f"\n\tOperación invalida el denominador no puede ser cero")
else:
    print(f"\n\tLa división de {val1} entre {val2} es: {val1 / val2}")

# 09 
print(f"\n\tEl resulado de {val1} a la {val2} potencia es: {val1 ** val2}")

# 10
if val2 <= 0:
    print(f"\n\tOperación invalida el denominador no puede ser cero")
else:
    entero = val1 // val2
    print(f"\n\tLa división entera de {val1} entre {val2} es: {entero}")

# 11
if val2 <= 0:
    print(f"\n\tOperación invalida el denominador no puede ser cero")
else:
    print(f"\n\tEl módulo de {val1} entre {val2} es: {val1 % val2}")

# 12
nota1 = float(input("\nIngresa tu primera nota: "))
nota2 = float(input("Ingresa tu segunda nota: "))
nota3 = float(input("Ingresa tu tercera nota: "))
prom = (nota1 + nota2 + nota3) / 3
print(f"\tEl promedio es: {prom}")

# 13
nums = [5, 12, 20, 15]
res = 0
print(f"\nConsiderando los valores: {nums} y los pesos: ", end=' ')
for i in range(1, 5):
    res += nums[i-1] * i
    print(f"{i}", end=' ')
res /= 4
print(f"\n\tEl resultado del promedio ponderado es: {res}")

# HW 03 - Editando textos
print("\n\nEDITANDO TEXTOS")
# 14
frase1 = "     This is an Optimen dev saying hi "
print(f"\t{frase1}")

# 15
frase = input("\nIngresa una frase: ")
print(f"\tTu frase es: {frase}")

# 16
print(f"\n\tTu frase es: {frase.upper()}")

# 17 
print(f"\n\tTu frase es: {frase.lower()}")

# 18
print(f"\n\t{frase1.strip()}")

# 19
print(f"\n\t{frase.strip()}")

# 20
print(f"\n\t{frase.strip().lower()}")

# 21
print(f"\n\t{frase.replace('e', 'f')}")

# 22
print(f"\n\t{frase.replace('a', chr(64))}")

# 23
print(f"\n\t{frase.replace('s', chr(36))}")


if __name__ == "__main__":
    print("\n\nYou're on exercises_02.py file")
